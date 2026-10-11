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
