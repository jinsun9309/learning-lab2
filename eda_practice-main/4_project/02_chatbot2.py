# 필요한 라이브러리 임포트
import streamlit as st
from openai import AzureOpenAI

# 환경변수 또는 직접 입력으로 설정값 가져오기
azure_endpoint = "https://internal-apigw-kr.hmg-corp.io/hchat-in/api/v2/01K6ET0Y7FMK2PN72HDMZ4P9W6"
api_key = "OYlOck5vnTLYUF7iE2hmeZlK2Z84bR0gLsSwC5em4zyDIpBSvzQXChRDaBopvWw"


# AzureOpenAI 클라이언트 초기화
client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    api_version="2024-10-21"
)

# Streamlit 앱 제목
st.title("💬 LLM 챗봇 만들기")

# ----------------
# 세션 상태 초기화
# ----------------
if "history" not in st.session_state:
    st.session_state["history"] = [
        {"role": "assistant", "content": "안녕하세요! 궁금한 점을 입력해주세요."}
    ]
if "email_mode" not in st.session_state:
    st.session_state["email_mode"] = False

# ----------------
# 이메일모드 on/off 버튼 UI 및 안내문
# ----------------
with st.sidebar:
    # 이메일 모드 전환 버튼
    if st.session_state["email_mode"]:
        if st.button("이메일 모드 종료", use_container_width=True):
            st.session_state["email_mode"] = False
    else:
        if st.button("이메일 모드 시작", use_container_width=True):
            st.session_state["email_mode"] = True
    
    st.markdown("---")
    st.markdown(
        "ℹ️ **이메일 모드 안내**\n\n"
        "- 버튼을 클릭하면, 입력 내용을 비즈니스 이메일 형태로 작성해줍니다.\n"
        "- 일반 챗봇 모드로 언제든 돌아올 수 있습니다."
    )

# 이메일 모드 활성화 시 상단 안내 출력
if st.session_state["email_mode"]:
    st.info("📧 **이메일 모드가 활성화되었습니다**\n- 이제 챗봇은 모든 답변을 공식적인 업무용 이메일로 작성합니다.")




# ----------------
# 대화 기록 출력 함수
# ----------------
def display_chat():
    for msg in st.session_state["history"]:
        if msg["role"] == "user":
            st.chat_message("user").markdown(msg["content"])
        else:
            st.chat_message("assistant").markdown(msg["content"])

display_chat()

# ----------------
# 입력창
# ----------------
user_input = st.chat_input(
    "메시지를 입력하세요."
)

# ----------------
# LLM 응답 생성 함수
# ----------------
def get_llm_response(messages, email_mode=False):
    # 이메일 모드이면 시스템 프롬프트 추가
    if email_mode:
        system_prompt = {
            "role": "system",
            "content": (
                "앞으로 요청받는 모든 내용을, 목적에 맞는 공식적이고 간결한 한국어 업무용 이메일로 작성하세요. "
                "이메일 서식(인사말, 마무리, 서명 등)도 넣어주고, 요구/질문이 불분명하면 추가로 명확한 정보를 질문하세요."
            )
        }
        # 프롬프트 최상단에 system 프롬프트 배치
        prompt_messages = [system_prompt] + messages
    else:
        prompt_messages = messages
        
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=prompt_messages
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = f"⚠️ 오류가 발생했습니다: {str(e)}"
    return answer

# ----------------
# 입력 처리 및 챗봇 응답
# ----------------
if user_input:
    # 대화 기록에 사용자 입력 추가
    st.session_state["history"].append({"role": "user", "content": user_input})
    display_chat()

    # LLM 응답 생성 (모드에 따라 프롬프트 다르게)
    bot_message = get_llm_response(
        st.session_state["history"],
        email_mode=st.session_state["email_mode"]
    )

    # 대화 기록에 assistant 답변 추가
    st.session_state["history"].append(
        {"role": "assistant", "content": bot_message}
    )

display_chat()
