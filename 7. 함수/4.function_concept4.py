# Lambda함수
'''
    - 간단한 함수가 있는 경우, 한줄짜리 함수로 간편하게 사용가능
'''

def add(a, b):      #input
    return a + b    #구현
print(add(3, 5))

f = lambda a, b: a + b  #input : 구현
print(f(3, 5))

def get_length(s):
    return len(s)

# 글자 길이에 따른 정렬
strings = ['Meet', 'themost', 'rugged', 'and']
strings.sort(key=lambda s:len(s))
print(strings)

# 수학 계산
import math
number = 3.14
print(abs(number))          #절대값
print(math.ceil(number))    #올림
print(math.floor(number))   #내림

print(math.sin(number))     #sin
print(math.cos(number))     #cos

