'''
    순신은 lily라는 이름의 교환학생과 친해지게 되었습니다.
    영어를 잘하지 못하는 순신은 lily에게 한국어를 가르쳐 주기 위해 한국어 연습 프로그램을 만들게 되었습니다.
        - 연습할 한국어가 담긴 리스트를 만든다
        - 리스트에서 순서대로 단어를 가져와 화면에 출력한다.
        - 프로그램 사용자는 단어를 그대로 입력하고

        Let's Learning Korean
        사랑해
        사랑해
        귀엽다
        귀엽다
        고마워
        고마워
        행복해
        햄복해
'''


korean = ["사랑해", "귀엽다", "고마워", "행복해"]
print("Let's Learning Korean")

for list in korean:
    print(list)
    x =input()
    if x != list:
        break
count = 1
print("전체 문제 개수 : ",(len(korean)),"개")
print("맞힌 문제 개수 : ",(len(x)-count),"개")
print("틀린 문제 개수 : ",(len(korean)) -(len(x)-count) ,"개")
# 전체 문제 개수 : 4개     len(korean) print((len(earPods)))
# 맞힌 문제 개수 : 2개
# 틀린 문제 개수 : 2개