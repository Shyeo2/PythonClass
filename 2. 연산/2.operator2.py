# 비교연산
print( 2 > 3)  #False
print(15 < 30) #True
print(1.5 >= 0) #True
print(2.5 <= 2.5) #True
print("주변음" == "주변소음") #False
print("1111111111" == "1111111111") #True

# 논리연산
print(4 < 6 and 10 >= 10)  #True and True --> True
print("적용형 주변음 허용 모드" != "적용형 주변음 허용 모드" or "나는 할 수 있다." == "나는 할 수 있다.")  #False or True --> True
print(not 5 == 5) #not True --> False

# 멤버십 연산자
# in - 포함되어있다.
# not in - 포함되어있지않다.
print("a" in "abc") #True
print("d" not in "abc") #True
