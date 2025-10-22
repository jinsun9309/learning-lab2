def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a/b

def main():
    while True:
        print("\n===== 계산기 메뉴 =====")
        print("1. 더하기 (a + b)")
        print("2. 빼기 (a - b)")
        print("3. 곱하기 (a * b)")
        print("4. 나누기 (a / b)")
        print("5. 종료")
        choice = input("사용할 기능의 번호를 입력하세요: ")

        if choice == '5':
            print("프로그램을 종료합니다.")
            break

        # 숫자 입력 받기
        try:
            a = float(input("첫 번째 숫자를 입력하세요: "))
            b = float(input("두 번째 숫자를 입력하세요: "))
        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력해 주세요.")
            continue

        if choice == '1':
            result = add(a, b)
            print(f"결과: {a} + {b} = {result}")
        elif choice == '2':
            result = subtract(a, b)
            print(f"결과: {a} - {b} = {result}")
        elif choice == '3':
            result = multiply(a, b)
            print(f"결과: {a} * {b} = {result}")
        elif choice == '4':
            result = divide(a, b)
            print(f"결과: {a} / {b} = {result}")
        else:
            print("올바른 번호를 선택해 주세요.")

if __name__ == "__main__":
    main()