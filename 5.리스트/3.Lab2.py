'''
    턱걸이 평균 측정 프로그램을 만들어 보시오.
    먼저, 턱걸이 횟수를 저장할 빈 리스트를 만드시오.
    그리고 일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장하시오.
    리스트에 저장된 데이터의 평균을 구해 출력하시오.

    예)
        1일차 턱걸이 횟수 >>>
        2일차 턱걸이 횟수 >>>
        3일차 턱걸이 횟수 >>>
        4일차 턱걸이 횟수 >>>
        5일차 턱걸이 횟수 >>>
        6일차 턱걸이 횟수 >>>
        7일차 턱걸이 횟수 >>>
'''
#방법1
# 턱걸이 횟수를 저장할 빈 리스트를 만드시오.
count = []
print(count)

# 일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장하시오.
day1 = int(input("1일차 턱걸이 횟수 >>>"))
day2 = int(input("2일차 턱걸이 횟수 >>>"))
day3 = int(input("3일차 턱걸이 횟수 >>>"))
day4 = int(input("4일차 턱걸이 횟수 >>>"))
day5 = int(input("5일차 턱걸이 횟수 >>>"))
day6 = int(input("6일차 턱걸이 횟수 >>>"))
day7 = int(input("7일차 턱걸이 횟수 >>>"))

count = [day1, day2, day3, day4, day5, day6, day7]
print(count)

# 리스트에 저장된 데이터의 평균을 구해 출력하시오.
count_sum = day1 + day2 + day3 + day4 + day5 + day6 + day7
day_count = 7
count_avg =int( count_sum / day_count)
print()

# 방법2
data = []

x = int(input("1일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("2일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("3일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("4일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("5일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("6일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("7일차 턱걸이 횟수 >>>"))
data.append(x)

total = data[0] +  data[1] +  data[2] +  data[3] +  data[4] +  data[5] +  data[6]
avg = total / 7

print("턱걸이 평균 횟수 >>>", int(avg))