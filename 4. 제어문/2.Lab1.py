# 회사를 그만두게 된 선혜는 유튜브를 시작하게 되었습니다.
# 유튜브를 통해서 수익창출을 하려고 합니다.
# 프로그램 사용자로부터 현재 구독자 수를 입력 받으면,
# 수익 창출이 가능한지 불가능한지 알려주는 프로그램을 작성해 보시오.
# (단, 수익창출은 구독자가 1000명 이상일 경우 가능하다)

# ex)현재 구독자수를 입력하세요 >>> 1200
#    수익 창출이 가능합니다!

# ex)현재 구독자수를 입력하세요 >>> 800
#    수익 창출이 불가능합니다!

sub_cnt = 1000
input_cnt =int(input("현재 구독자수를 입력하세요 >>>"))
if sub_cnt <= input_cnt :
    print("수익 창출이 가능합니다!")
elif sub_cnt >= input_cnt :
    print("수익 창출이 불가능합니다.")

