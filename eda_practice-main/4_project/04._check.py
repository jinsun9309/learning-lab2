import pyautogui
import time

# 작업 시작 전 3초 대기 (사용자가 입력창을 미리 선택할 수 있게)
print("3초 뒤에 숫자 입력을 시작합니다. 입력창을 미리 클릭하세요.")
time.sleep(1)  # 0초 기다리기

for i in range(1, 11):
    pyautogui.typewrite(str(i))  # 숫자 i를 문자열 형태로 입력
    pyautogui.press('enter')     # 엔터키 입력 (필요 없으면 삭제 가능)
    time.sleep(0.3)              # 입력 간 딜레이 (0.3초)

    try:
    while True:
        x, y = pyautogui.position()      # 현재 마우스 좌표 가져오기
        print(f"X: {x}, Y: {y}", end='\r') # 좌표를 실시간으로 출력 (커서 안 깜빡이게)
        time.sleep(0.1)                   # 0.1초마다 출력 (속도 조절 가능)
except KeyboardInterrupt:
print("\n프로그램을 종료합니다.")