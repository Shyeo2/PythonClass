# 비만도 계산기를 만들어 보시오.
'''
예시 )
        BMI 계산기 입니다.
        신장: (입력)
        몸무게: (입력)
        BMI:

'''
print("BMI계산기입니다.")
height = int(input("신장: "))
weight = int(input("몸무게:"))
BMI = int (weight / (height * height) * 10000)
print("BMI:", BMI)
