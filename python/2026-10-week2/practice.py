# 2026년 10월 2주차 연습 — 자료형, input
# 코랩에서 직접 풀고, 완성된 코드를 여기에 옮겨 적는다.

# ===== 1일차 (2026-10-07): 자료형 — 숫자 vs 문자열 =====

# 1단계: 안 보고 타이핑
type(3.5)                  # 아무것도 안 나옴 — 알아내기만 하고 보여주지 않음
print(type(3.5))           # <class 'float'>

print("Do" + "Re")         # DoRe
print("Am " *4)            # Am Am Am Am   ← 따옴표 안 공백도 반복

# 2단계: 예측 문제
# 문제 1 (정답)
print(10 + 20)             # 30
print("10" + "20")         # 1020  ← 문자열은 이어 붙이기

# 문제 2 (오답: float로 예측)
print(type("3.5"))         # <class 'str'>  ← 따옴표가 있으면 문자열

# 문제 3 (정답)
chord = "C"
print(chord * 2 + "G")     # CCG  ← * 먼저

# 문제 4: 에러 추측 (정답 — 타입이 달라서)
# print("BPM " + 120)      # TypeError: can only concatenate str (not "int") to str
