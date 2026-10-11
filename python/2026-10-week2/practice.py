# 2026년 10월 2주차 연습 — 자료형, input
# 코랩에서 직접 풀고, 완성된 코드를 여기에 옮겨 적는다.

# ===== 1일차 (2026-10-07): 자료형 — 숫자 vs 문자열 =====

# 1단계: 안 보고 타이핑
type(3.5)                  # 아무것도 안 나옴 — 알아내기만 하고 보여주지 않음
print(type(3.5))           # <class 'float'>

print("Data" + "Science")  # DataScience
print("NA " *4)            # NA NA NA NA   ← 따옴표 안 공백도 반복

# 2단계: 예측 문제
# 문제 1 (정답)
print(10 + 20)             # 30
print("10" + "20")         # 1020  ← 문자열은 이어 붙이기

# 문제 2 (오답: float로 예측)
print(type("3.5"))         # <class 'str'>  ← 따옴표가 있으면 문자열

# 문제 3 (정답)
grade = "A"
print(grade * 2 + "B")     # AAB  ← * 먼저

# 문제 4: 에러 추측 (정답 — 타입이 달라서)
# print("매출 " + 120)     # TypeError: can only concatenate str (not "int") to str

# 보너스: 문제 4 고치기 → 매출 120
print("매출", "120")        # 방법 1: 쉼표는 공백 자동 (print("매출", 120)도 가능)
print("매출 " +"120")       # 방법 2: + 는 공백 없음 → "매출 " 안에 직접 공백


# ===== 2일차 (2026-10-07): 형 변환 str(), int() =====

# 복습 (예측 모두 정답)
visitors = 50
print(visitors + 10)       # 60
print(visitors)            # 50  ← 보여주기만 했으니 그대로
visitors = visitors + 10
print(visitors)            # 60

print(type(7))             # <class 'int'>
print(type("7"))           # <class 'str'>
print(type("Seoul"))       # <class 'str'>

# 타이핑
sales = 90
print("매출 " + str(sales))   # 매출 90
print(int("7")+int("3"))     # 10  (int 없으면 73)

# 문제 1 (정답)
x = "5"
print(x * 3)               # 555  ← 문자열 반복
print(int(x) * 3)          # 15   ← 숫자 곱셈

# 문제 2 (정답)
print(type(str(100)))      # <class 'str'>
print(type(int("100")))    # <class 'int'>

# 문제 3: + 만으로 "총 210초" (정답)
minutes = 3
seconds = 30
print("총 "+str(minutes*60+seconds)+"초")

# 문제 4: 에러 추측 (정답 — 정수 모양이 아니라서)
# print(int("N/A"))        # ValueError: invalid literal for int() with base 10: 'N/A'


# ===== 3일차 (2026-10-07): input =====

# 복습 (모두 정답)
a = "4"
b = 4
print(a * 2)               # 44
print(b * 2)               # 8
print(int(a) + b)          # 8

item = "A"
stock = 140
print(item+"상품 "+str(stock)+"개")   # A상품 140개

# print("Week " + 3)       # TypeError
# print(int("1,000"))      # ValueError — 쉼표 들어간 숫자 문자열도 int() 불가

# 타이핑
name = input("이름: ")
print(name +"님 안녕하세요")

price = input("가격: ")
print(int(price)*2)        # 쓸 때 변환 (받자마자: price = int(input("가격: ")))

# 문제 1: 7 입력 (정답)
x = input("숫자: ")
print(x + x)               # 77
print(int(x) + int(x))     # 14

# 문제 2: 분·초 입력 → 총 몇 초 (정답)
minutes = input("분: ")
seconds = input("초: ")
print("총",str(int(minutes)*60+int(seconds))+"초")   # 총 135초 ← 쉼표(공백) + +(붙이기) 섞기

# 문제 3: 기호 반복으로 구분선 만들기 (정답)
symbol = input ("기호: ")
times = input ("횟수: ")
print(symbol*int(times))   # - 와 3 입력 → --- ← 횟수만 int

# 문제 4: 에러 추측 (정답)
quantity = input("수량: ")
# print(quantity + 10)     # TypeError: can only concatenate str (not "int") to str
print(int(quantity) + 10)  # 고친 코드

# ===== 4일차 (2026-10-11): 불(bool), 비교 연산자 =====

# 복습 1: 예측 (3 입력)
order = input("주문 수량: ")
print(order * 2)           # 33
print(int(order) * 2)      # 6
print(type(order))         # <class 'str'>  ← 처음엔 int로 예측(오답). int(order)는 잠깐 쓰기만, order는 그대로

# 복습 2: 단가·수량 입력 → 총액 (힌트 후 정답)
price = int(input("단가: "))
quantity = int(input("수량: "))
# print("총액",price*quantity+"원")   # TypeError — 숫자 + 문자열
print("총액",str(price*quantity)+"원")  # 총액 6000원 ← 받자마자 int로 바꿨어도 붙일 땐 다시 str

# 타이핑
temperature = 28
print(temperature>=30)     # False

user_count = 0
print(user_count==0)       # True

# 문제 1: 예측
sales = 120
target = 100
print(sales > target)      # True
print(sales == 120)        # True
print(sales != target)     # True
print(type(sales > target))   # <class 'bool'>  ← 처음엔 str로 예측(오답). True엔 따옴표 없음

# 문제 2: 예측
print(10 == 10)            # True
print("10" == 10)          # False  ← 처음엔 "오류"로 예측(오답). ==는 묻기만 → 종류 달라도 에러 없이 False
print(int("10") == 10)     # True

# 문제 3: 60점 이상이면 합격 (힌트 후 정답)
score = int(input("점수: "))
# print("합격여부:", score >=75)       # 띄어쓰기 누락 + 예시 입력 75를 기준으로 씀
print("합격 여부:", score >= 60)       # 합격 여부: True

# 문제 4: 에러 추측 (정답)
stock = 5
# print(stock = 0)         # TypeError: print() got an unexpected keyword argument 'stock'
print(stock == 0)          # False ← 비교는 ==
