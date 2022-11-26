'''
    로또 예상번호 추출 프로그램을 구현하려고 합니다.
    다음 조건에 따라 프로그램을 완성해 보시오.
        1) 로또 번호 6개를 생성한다
        2) 로또 번호는 1~45까지의 랜덤한 번호다
        3) 6개의 숫자 모두 달라야 한다
        4) get_random_number() 함수를 사용해서 구현한다

        출력 예) 1 8 11 13 26 42

        - 리스트 사용
        - 반복문 사용
        - 조건문 사용 (중복여부)
        - 정렬 (sort)
'''

import random
def get_random_number():
    number = random.randint(1,45)
    return number
# 로또 번호를 저장할 리스트
lotto_list = []
print(lotto_list)


while True:
    if (len(lotto_list)) == 6:
        break
    random_number = get_random_number()
    if random_number not in lotto_list:
        lotto_list.append(random_number)

lotto_list.sort()
for x in lotto_list:
    print(x , end=" ")