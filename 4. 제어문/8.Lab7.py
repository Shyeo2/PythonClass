'''
    사용자로부터 국어, 수학, 영어 성적이 입력됩니다.
    세 과목의 평균점수가 80점 이상이면 합격입니다.
    그런데 프로그램의 오류가 발생했습니다.
    80점 이상일 경우 불합격이 표시되도록 프로그램을 작성해 보시오.
    (단, 0점에서 100점 사이의 숫자를 입력하지 않으면 "잘못 입력했습니다."를 출력하시오)

    예시)
        국어 >>>
        수학 >>>
        영어 >>>

        불합격             합격              잘못입 력했습니다
'''

Kor = int(input("국어 >>>"))
Mat = int(input("수학 >>>"))
Eng = int(input("영어 >>>"))

#방법1
score_sum = Kor + Mat + Eng
score_avg = score_sum / 3
if 0 <= Kor <= 100 and 0 <= Mat <= 100 and 0 <=Eng <= 100 :
    if score_avg >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력했습니다.")

#방법2
if Kor < 0 or Kor > 100 or Mat < 0 or Mat > 100 or Eng < 0 or Eng > 100:
    print("잘못 입력했습니다.")
elif score_avg >=80:
    print("불합격")
else:
    print("합격")