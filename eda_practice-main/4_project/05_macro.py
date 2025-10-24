import pyautogui
import time

# 각 입력 필드 및 버튼의 (x, y) 좌표를 직접 확인해서 입력하세요.
START_YEAR_POS = (100, 200)     # 시작년도 박스 좌표
START_MONTH_POS = (100, 250)    # 시작월 박스 좌표
END_YEAR_POS = (200, 200)       # 종료년도 박스 좌표
END_MONTH_POS = (200, 250)      # 종료월 박스 좌표
SEARCH_BTN_POS = (300, 400)     # 검색 버튼 좌표
EXCEL_DOWNLOAD_POS = (350, 500) # 엑셀파일 다운로드 버튼 좌표

def macro():
    print("3초 뒤에 매크로 실행 시작합니다. 창을 미리 열어두세요.")
    time.sleep(3)


def month_click(start_m, end_m):

    # 1. 시작년도 클릭 -> 입력(2023) -> 엔터
    pyautogui.click(START_YEAR_POS)   #클릭
    pyautogui.typewrite('2023')      #키보드입력
    pyautogui.press('enter')
    time.sleep(0.2)

    # 2. 시작월 클릭 -> 입력(01) -> 엔터
    pyautogui.click(START_MONTH_POS)
    pyautogui.typewrite('01')
    pyautogui.press('enter')
    time.sleep(0.2)

    # 3. 종료년도 클릭 -> 입력(2025) -> 엔터
    pyautogui.click(END_YEAR_POS)
    pyautogui.typewrite('2025')
    pyautogui.press('enter')
    time.sleep(0.2)



    # 4. 종료월 클릭 -> 입력(06) -> 엔터
    pyautogui.click(END_MONTH_POS)
    pyautogui.typewrite('06')
    pyautogui.press('enter')
    time.sleep(0.2)


def download():
    # 5. 검색버튼 클릭 -> 기다리기(5초)
    pyautogui.click(SEARCH_BTN_POS)
    time.sleep(5)

    # 6. 엑셀 다운로드 버튼 클릭 -> 기다리기(1초) -> 엔터
    pyautogui.click(EXCEL_DOWNLOAD_POS)
    time.sleep(1)
    pyautogui.press('enter')
    print("매크로 작업이 완료되었습니다.")

#반복하고 싶은 년도
years = [2023,2024,2025] 
#시작달
start_ms = [1,7]
#끝달
end_ms =[6,12]
month_pair = [(1,6), (7,12)]


for year in years:
    print("3초 뒤에 매크로 실행 시작합니다. 창을 미리 열어두세요.")
    time.sleep(3)

    year_click(year)
    
    for pair in month_pair:
        



if __name__ == "__main__":
    macro()
