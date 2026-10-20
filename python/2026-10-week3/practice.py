# 2026년 10월 3주차 연습 — 조건문, 반복문
# 코랩/Programiz에서 직접 풀고, 완성된 코드를 여기에 옮겨 적는다.

# ===== 1일차 (2026-10-11): 조건문 if =====

# 타이핑 (IndentationError 스스로 해결)
stock = 0

# ··if stock == 0:         # IndentationError: unexpected indent ← if 줄은 들여 쓰지 않는다
if stock == 0:
  print("품절")             # 2칸도 동작, 표준은 4칸
print("확인 끝")
# stock = 5이면 → 확인 끝 만 출력

# 문제 1: 예측 (정답)
score = 55
if score >= 60:
    print("합격")
    print("축하합니다")
print("채점 완료")          # 채점 완료

# 문제 2: 예측 (정답) — 한 줄만 밖으로
score = 55
if score >= 60:
    print("합격")
print("축하합니다")         # 축하합니다  ← if 밖이라 항상 실행
print("채점 완료")          # 채점 완료

# 문제 3: 50000원 이상 무료 배송 (안내문 공백만 힌트 후 수정)
order_price = int(input("주문 금액: "))   # "주문 금액:" → 입력과 붙어 보임
if order_price >= 50000:
  print("무료 배송")
print("주문 접수")

# ===== 3일차 (2026-10-19): 복습 + elif =====

# 복습 2: 학생 수 → 강의실 (처음엔 양쪽에 print → room에 값만 넣도록 수정)
student_count = int(input("학생 수: "))   # "학생 수:" 공백 누락 → 수정
if student_count >= 20:
    room = "큰 강의실"
else:
    room = "작은 강의실"
print("배정된 강의실:", room)            # str(room) 필요 없음: 이미 글자

# elif 타이핑: 미세먼지 등급 (100 → 나쁨, 50 → 보통, 20 → 좋음)
dust = int(input("미세먼지 농도: "))
if dust >= 81:
    grade = "나쁨"
elif dust >= 31:
    grade = "보통"                        # grade ='' "보통" 오타 → 수정
else:
    grade = "좋음"
print("미세먼지:", grade)

# 문제 2: 예측 (정답) — 순서 함정
score = 95
if score >= 60:
    grade = "C"                           # 처음 True → 여기서 끝
elif score >= 80:
    grade = "B"
elif score >= 90:
    grade = "A"
else:
    grade = "F"
print("학점:", grade)                     # 학점: C

# 문제 3: 점수 → 학점 (한 번에 정답)
score = int(input("점수: "))

# 큰 기준부터 검사해야 함 (작은 기준이 위에 있으면 95점도 C가 됨)
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print("학점:", grade)

# ===== 4일차 (2026-10-20) =====

# 복습 1: 예측 — else가 없으면 다 False일 때 아무것도 안 함
stock = 0
if stock >= 10:
    print("재고 넉넉")
elif stock >= 1:
    print("재고 부족")
print("확인 완료")                        # 확인 완료 (확인완료 → 공백 힌트 후 정답)

# 복습 2: 구매 금액 할인 (구조 한 번에 정답, 안내문 공백 힌트 후 수정)
purchase_amount = int(input("구매 금액: "))

if purchase_amount >= 100000:
    discount = 10000
elif purchase_amount >= 50000:
    discount = 3000
else:
    discount = 0

payment_amount = purchase_amount - discount
print("결제 금액",str(payment_amount)+"원")

# for 타이핑: 들여 쓴 줄만 반복
for i in range(1, 4):
    print(i, "번째 반복")                 # 3번
print("반복 끝")                          # 1번

# 문제 1: 예측 — 줄 0 / 줄 1 / 줄 2 / 끝 (처음엔 0줄로 순서 오답)
for i in range(3):
    print("줄", i)
print("끝")

# 문제 2: 예측 (정답) — 20 / 30 / 40
for i in range(2, 5):
    print(i * 10)

# 문제 3: 구구단 (X → x, str() 빼기 힌트 후 정답)
number = int(input("단: "))

for i in range(1,10):
    print(number,"x",i,"=" ,number*i)

# 문제 4: 학생 3명 등급 + 총점 (총점 score(i) → 누적 패턴 힌트 후 정답)
total_score = 0

for i in range(1,4):
    score = int(input(str(i)+"번 학생 점수: "))
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"
    
    print(str(i)+"번 학생",grade)
    total_score = total_score + score
print("총점",total_score)
