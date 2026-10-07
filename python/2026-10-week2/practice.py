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

# 보너스: 문제 4 고치기 → BPM 120
print("BPM", "120")        # 방법 1: 쉼표는 공백 자동 (print("BPM", 120)도 가능)
print("BPM " +"120")       # 방법 2: + 는 공백 없음 → "BPM " 안에 직접 공백


# ===== 2일차 (2026-10-07): 형 변환 str(), int() =====

# 복습 (예측 모두 정답)
volume = 50
print(volume + 10)         # 60
print(volume)              # 50  ← 보여주기만 했으니 그대로
volume = volume + 10
print(volume)              # 60

print(type(7))             # <class 'int'>
print(type("7"))           # <class 'str'>
print(type("Am"))          # <class 'str'>

# 타이핑
bpm = 90
print("BPM " + str(bpm))   # BPM 90
print(int("7")+int("3"))   # 10  (int 없으면 73)

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
# print(int("Am"))         # ValueError: invalid literal for int() with base 10: 'Am'
