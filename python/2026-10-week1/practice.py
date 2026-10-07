# 2026년 10월 1주차 연습 — print, 변수
# 코랩에서 직접 풀고, 완성된 코드를 여기에 옮겨 적는다.

# ===== 1일차 (2026-09-29): print =====

# 안 보고 타이핑
print("Kyungeon")
print(12*5)
print("서울", "부산", "대구", "광주")   # 따옴표 밖 쉼표 = 구분 기호 → 서울 부산 대구 광주

# 문제 1: 두 줄 출력
print("안녕하세요")
print("저는 경언입니다.")

# 문제 2: 3분 30초는 몇 초?
print("3분 30초=", 3*60+30)

# 문제 3: print 한 번으로 글자 + 계산 섞기
print("단가 120원의 두 배는", 120*2)


# ===== 2일차 (2026-10-07): 1일차 안 보고 다시 짜기 =====

# A: 서울 부산 대구 광주 출력
print("서울", "부산", "대구", "광주")

# B: 1분 45초는 몇 초?
print("1분 45초=", 60*1+45)

# C: 출력 예측 문제 (예측이 틀렸던 문제)
print("서울,부산,대구", "광주")   # 서울,부산,대구 광주  ← 안 쉼표는 글자, 밖 쉼표는 공백 한 칸
print("2+3", 2+3)                # 2+3 5               ← 밖 쉼표는 화면에 안 나온다


# ===== 2일차 (2026-10-07): 변수 =====

# 안 보고 타이핑
product = "notebook"
print(product)     # notebook  ← 따옴표 안은 대소문자 그대로

stock = 120
print(stock*2)     # 240
stock = 90
print(stock)       # 90  ← 다시 넣으면 바뀐다

# 문제 1: 변수 이름만으로 총 초 계산
minutes = 3
seconds = 30
print("총 초=", minutes*60+seconds)   # 처음엔 쉼표를 빠뜨려 SyntaxError → 고침

# 문제 2: 출력 예측 (정답)
city = "Seoul"
print("city", city)              # city Seoul
print(city, "Busan", "Daegu")    # Seoul Busan Daegu

# 문제 3: 출력 예측 (정답)
stock = 100
stock = stock + 20   # 오른쪽 먼저: 100 + 20 → stock에 다시 넣음
print(stock)         # 120


# ===== 3일차 (2026-10-07): 변수 안 보고 다시 짜기 =====

# A: 4분 15초는 몇 초?
minutes = 4
seconds = 15
print("총 초=", minutes*60 + seconds)   # 처음엔 "총 초"로 써서 = 누락 → 출력 형식 맞춤

# B: 재고 20 올리기
stock = 100
print(stock+20)      # 120 — 보여주기만 함, stock은 여전히 100
stock = stock + 20   # 실제로 값을 바꾸는 방법
print(stock)         # 120

# C: 출력 예측 (정답)
name = "Kyungeon"
print("name", name)        # name Kyungeon

# D: 쉼표 예측 (정답)
grade = "A"
print("Grade,", grade, "level")   # Grade, A level  ← 안 쉼표는 글자
print(grade, "=", 90)             # A = 90
