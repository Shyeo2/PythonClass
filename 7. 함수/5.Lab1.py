'''
    세 개의 정수를 인자로 받아,
    합계와 평균을 출력해주는 함수를 만드시오.

    예) 합계:   평균:
'''

def function(a, b, c):
    sum = a + b + c
    avg = int(sum / 3)
    print("합계 :" , sum , "평균:" , avg)

function(3, 5, 7)

# 설명문 (docstring) """ """
# 문자열 포매팅(f"{변수명}")
def print_sum_avg(x, y, z):
    """
    세 개의 숫자를 받아 합계와 평균을 출력하는 함수
    :param x:
    :param y:
    :param z:
    :return:
    """

    sum = x + y + z
    avg = sum / 3
    print(f"합계: {sum} 평균: {avg}")

print_sum_avg(10, 20, 30)