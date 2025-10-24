# 필요한 라이브러리 import
import streamlit as st
from openai import AzureOpenAI   # 최신 OpenAI Azure SDK 사용

# 1. LLM API 인증 및 설정 (환경변수에서 불러오는 방식 권장)
azure_endpoint = "https://internal-apigw-kr.hmg-corp.io/hchat-in/api/v2/01K6ET0Y7FMK2PN72HDMZ4P9W6"
api_key = "OYlOck5vnTLYUF7iE2hmeZlK2Z84bR0gLsSwC5em4zyDIpBSvzQXChRDaBopvWw"
api_version = "2024-10-21"   # 최신 버전 지정

# 2. OpenAI 클라이언트 생성
client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    api_version=api_version
)

# 3. Streamlit 앱 UI 기본 설정
st.set_page_config(page_title="LLM 챗봇", page_icon="🤖")

st.title("AI 챗봇 (AzureOpenAI + Streamlit)")
st.markdown("질문을 입력하면 LLM으로부터 실시간 답변을 받아보세요.")

# 4. 대화 내역을 session_state에 저장 (페이지 새로고침 시에도 대화 유지)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []   # [ {"role": "user/assistant", "content": "..."} ]

# 5. 사용자 입력 받기
user_input = st.text_input("메시지를 입력하세요", key="input")

# 6. 메시지 처리 및 LLM API 호출
if st.button("보내기") and user_input:
    # 1) 사용자의 메시지 chat_history에 추가
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input}
    )
    # 2) LLM API의 메시지 포맷에 맞게 구성
    messages = [
        {"role": msg["role"], "content": msg["content"]}
        for msg in st.session_state.chat_history
    ]
    # 3) API 호출: 응답 생성
    try:
        completion = client.chat.completions.create(
            model="gpt-4.1",   # 모델명 지정
            messages=messages
        )
        answer = completion.choices[0].message.content  # 응답 추출
        # 4) 답변을 chat_history에 assistant 역할로 추가
        st.session_state.chat_history.append(
            {"role": "assistant", "content": answer}
        )
    except Exception as e:
        # 에러 발생 시 안내
        st.session_state.chat_history.append(
            {"role": "assistant", "content": f"[오류] {str(e)}"}
        )

# 7. 대화 내역 UI 표시 (최신순으로)
st.markdown("---")
st.subheader("대화 내역")
for i, msg in enumerate(st.session_state.chat_history):
    if msg["role"] == "user":
        st.markdown(f"**👤 사용자:** {msg['content']}")
    else:
        st.markdown(f"**🤖 챗봇:** {msg['content']}")

# 8. (선택) 대화 초기화 버튼
if st.button("대화 초기화"):
    st.session_state.chat_history = []
    st.experimental_rerun()

