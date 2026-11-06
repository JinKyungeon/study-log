# 2026년 10월 4주차 연습 — 점검과 복습 (새 개념 없음)
# 1·2일차 코드는 notes.md에 정리되어 있다.
# 3일차부터 Antigravity IDE에서 직접 짜고 실행한다.
#   칸 실행: # %% 위의 Run Cell (Jupyter 확장 + .venv) → 칸마다 따로 실행되니 주석 처리 필요 없음
#   전체 실행: 터미널에서 python3 python/2026-10-week4/practice.py (input이 모두 차례로 돈다)
#   터미널 맨 앞이 >>> 이면 파이썬 안 → exit() 후 실행

# ===== 3일차 (2026-11-06) =====

# %% 3일차 문제 1: 입장 확인 안 보고 다시 짜기 (질문·예시 후 정답)
allowed_count = 0

for i in range(1, 4):
    age = int(input(str(i)+"번 나이: "))
    # is_allowed = 13               ← 반복 밖에서 기준 숫자를 담음. is_ 에는 True/False가 와야 한다
    is_allowed = age >= 13          # 비교 결과(True/False)를 담는다. age 입력 "다음" 줄에 (위에 두면 NameError)
    if is_allowed:
        # print(str(i)+"번 입장가능")  ← 띄어쓰기 누락
        print(str(i)+"번 입장 가능")
        allowed_count = allowed_count + 1
    else:
        # print("보호자 필요")         ← 번호 누락
        print(str(i)+"번 보호자 필요")
print("입장 가능:", allowed_count, "명")
# 입력 15, 9, 13 → 1번 입장 가능 / 2번 보호자 필요 / 3번 입장 가능 / 입장 가능: 2 명

# %% 3일차 문제 2: 재고 예측 (표 채워서 정답, 출력 공백만 질문 후)
stock = 10
day = 0
while stock > 0:
    day = day + 1
    stock = stock - 4
    if stock <= 2:
        print(day, "일차 주문 필요")
    else:
        print(day, "일차 재고", stock)
print("총", day, "일")
# 예측:
# 1 일차 재고 6        ← 처음엔 "1일차" (쉼표 = 공백) → 질문 후 수정
# 2 일차 주문 필요     ← 2 <= 2 → True (경계값)
# 3 일차 주문 필요     ← stock이 -2가 돼도 그 바퀴는 끝까지
# 총 3 일              ← 마지막 검사 -2 > 0 → False → 밖으로 (스스로 표에 넣음)

# %% 3일차 문제 3: 주문 결제 (한 번에 정답)
price = int(input("단가: "))
quantity = int(input("수량: "))          # 처음엔 quantitiy (에러 없는 오타) → 스스로 수정
total_amount = price * quantity
is_free_shipping = total_amount >= 30000   # 문제 1에서 배운 is_ 를 바로 적용
shipping_fee = 3000

if is_free_shipping:                       # 블록 안에서는 값만 정하고
    payment_amount = total_amount
else:
    payment_amount = total_amount + shipping_fee

print("총액", str(total_amount)+"원")      # print는 밖에서 한 번. 쉼표(띄우기) vs +(붙이기)
print("무료 배송:", is_free_shipping)
print("결제 금액", str(payment_amount)+"원")
# 8000, 3 → 총액 24000원 / 무료 배송: False / 결제 금액 27000원
# 12000, 3 → 총액 36000원 / 무료 배송: True / 결제 금액 36000원
