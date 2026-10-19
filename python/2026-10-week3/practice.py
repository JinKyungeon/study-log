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
