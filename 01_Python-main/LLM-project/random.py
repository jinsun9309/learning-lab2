import streamlit as st
import random
import time

# 맛집 리스트
places = [
    "청담진쭈꾸미",
    "중앙식당",
    "봉산돼지국밥",
    "상남동보쌈",
    "육칼국수집",
    "상남김밥천국",
    "가격파괴왕 돈까스",
    "현덕분식",
    "수라상덮밥",
    "일미미니족발",
    "짜장마을",
    "명동반점",
    "스시마을",
    "카레한그릇",
    "포베트남",
    "왕돌판삼겹살",
    "진포한우곱창",
    "더하누",
    "카페 오를리",
    "루프탑 카페 블루문"
]

st.title("회식 랜덤 맛집 추천 룰렛 🎉")

# 룰렛 결과 보여줄 영역 (맛집 리스트 위에 위치)
roulette_spot = st.empty()

st.write("")  # 간격

st.subheader("전체 후보 맛집 리스트")
# 맛집 리스트 보여줄 영역
list_spot = st.empty()

# session_state 관련 변수
if 'final_choice' not in st.session_state:
    st.session_state.final_choice = None
if 'spinning' not in st.session_state:
    st.session_state.spinning = False

def spin_roulette():
    st.session_state.spinning = True
    st.session_state.final_choice = None

if st.button("회식장소 추천 룰렛 돌리기"):
    spin_roulette()

# 룰렛 도는 효과
if st.session_state.spinning:
    spin_times = 35  # 7초 동안 제법 돌려보자
    duration = 7.0 / spin_times
    for _ in range(spin_times):
        idx = random.randint(0, len(places) - 1)
        roulette_spot.markdown(
            f"<h2 style='color:orange'>{places[idx]}</h2>", unsafe_allow_html=True)
        time.sleep(duration)
    # 마지막 선택
    final_index = random.randint(0, len(places)-1)
    st.session_state.final_choice = places[final_index]
    roulette_spot.markdown(
        f"<h2 style='color:yellow;background:#080;padding:8px;border-radius:8px'>🎉 {st.session_state.final_choice} 🎉</h2>",
        unsafe_allow_html=True)
    st.session_state.spinning = False
    # 풍선 효과
    st.balloons()

# 리스트 다시 출력: 최종 선택된 곳은 색이 다름/굵게 표시
highlight_idx = None
if st.session_state.final_choice and st.session_state.final_choice in places:
    highlight_idx = places.index(st.session_state.final_choice)

list_markdown = ""
for i, p in enumerate(places, 1):
    if i-1 == highlight_idx:
        list_markdown += f"<p style='color:#fff;background:#FF9800;font-weight:bold;padding:6px;border-radius:6px'>{i}. {p}</p>\n"
    else:
        list_markdown += f"<p>{i}. {p}</p>\n"
list_spot.markdown(list_markdown, unsafe_allow_html=True)

if st.session_state.final_choice:
    st.success(f"오늘의 추천 회식 장소는: **{st.session_state.final_choice}** 입니다!")
