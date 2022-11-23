'''
    if
    if - else
    if - elif
    if - elif - else

    규황이는 강의를 8시간 동안 들으니, 배가 너무 고파서 저녁을 먹기로 하였습니다.
    규황이가 현재 가진 금액을 통해 최대로 먹을 수 있는 음식을 출력해 주는 프로그램을 작성해 보시오.
    조건)20000원 이상 : 치킨, 10000원 이상 : 떡볶이, 3000원 이상 : 편의점 김밥, 그 외 : 굶어요

'''

input_money = int(input("얼마 있어>>"))

if input_money >= 20000 :
    print("엽떡 먹자")
elif input_money >= 10000 :
    print("신전 먹자")
elif input_money >= 3000 :
    print("편의점 떡볶이 먹자")
else:
    print("배고파")