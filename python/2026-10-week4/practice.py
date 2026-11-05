# 2026년 10월 4주차 연습 — 점검과 복습 (새 개념 없음)
# 1·2일차 코드는 notes.md에 정리되어 있다.
# 3일차부터 Antigravity IDE에서 직접 짜고 터미널에서 실행한다.
#   실행: python3 python/2026-10-week4/practice.py

# ===== 3일차 (2026-11-06) =====
allowed_count = 0

for i in range(1,4):
    age = int(input(str(i)+"번 나이: "))
    is_allowed = age >=13
    if is_allowed:
        print(str(i)+"번 입장 가능")
        allowed_count = allowed_count + 1
    else:
        print(str(i)+"번 보호자 필요")
print("입장 가능:",allowed_count,"명")

    