# 2026년 11월 1주차 연습 — 리스트 [ ]
# 칸 실행: # %% 위의 Run Cell / 전체 실행: python3 python/2026-11-week1/practice.py

# ===== 1일차 (2026-11-09) =====

# %% 1일차 타이핑: 리스트 만들기·꺼내기·len·for 누적 (한 번에 정답)
daily_sales = [12000, 8500, 15000]
print(daily_sales[0])        # 번호는 0부터 → 첫 번째
print(daily_sales[2])        # 세 번째
print(len(daily_sales))      # 값 개수

total_sales = 0
for sales in daily_sales:    # 리스트를 바로 넣으면 값이 하나씩 sales에
    total_sales = total_sales + sales
print("총 매출", total_sales)
# 예측:
# 12000
# 15000
# 3
# 총 매출 35500

# %% 1일차 문제 1: 성적 예측 (표 정답, 위 두 줄은 질문 후)
scores = [80, 95, 70, 60]
print(scores[1])             # 95 ← 0부터 세서 두 번째
print(len(scores))           # 4
# print(scores[4])           # IndexError: list index out of range ← 번호는 0~3. 마지막 번호 = len - 1

pass_count = 0
for score in scores:
    if score >= 75:
        print(score, "통과")
        pass_count = pass_count + 1
print("통과 인원", pass_count)
# 예측 표 (바퀴 / score / score >= 75 / pass_count / 출력)
# 1 / 80 / True  / 1 / 80 통과
# 2 / 95 / True  / 2 / 95 통과
# 3 / 70 / False / 2 / (없음)
# 4 / 60 / False / 2 / (없음)
# 반복 뒤: 통과 인원 2

# %% 1일차 문제 2: 미세먼지 (결과 한 번에, 이름·len 질문 후 다듬기)
pm10_values = [45, 82, 30, 95, 60, 120, 38]
bad_day_count = 0
# day_count = 0  + 반복 안에서 day_count = day_count + 1   ← len()으로 이미 알 수 있는 값을 또 셈
day_count = len(pm10_values)
# average_pm10 = 0  (반복 안에서 합계를 담음)            ← 이름은 평균인데 실제로는 합계 → 읽는 사람이 헷갈림
total_pm10 = 0

print("측정 일수:", day_count)
for pm10 in pm10_values:
    if pm10 >= 80:                       # if 안: 나쁨인 날만
        bad_day_count = bad_day_count + 1
        print(pm10, "나쁨")
    total_pm10 = total_pm10 + pm10       # if 밖: 모든 날
average_pm10 = total_pm10 / day_count    # 평균은 반복이 끝난 뒤
print("나쁨 일수:", bad_day_count)
print("평균 농도:", average_pm10)
# 측정 일수: 7 / 82 나쁨 / 95 나쁨 / 120 나쁨 / 나쁨 일수: 3 / 평균 농도: 67.14285714285714

# %% 1일차 문제 3: 최고 점수 찾기 — 최댓값 패턴 (한 번에, 함정 질문 후 수정)
scores = [72, 88, 95, 64, 90]
# max_score = 0              ← [-5, -3, -9] 같은 기온이면 한 번도 안 바뀌어서 0 (리스트에 없는 값)
max_score = scores[0]        # 리스트 "안의" 값으로 시작. scores 줄보다 아래에 (위면 NameError)
for score in scores:
    if score > max_score:    # 지금까지 본 것보다 크면
        max_score = score    # 기억해 둔 값을 바꾼다
print("최고 점수:", max_score)
# [72, 88, 95, 64, 90] → 95 / [50, 40, 99, 10] → 99 / [-5, -3, -9] → -3
