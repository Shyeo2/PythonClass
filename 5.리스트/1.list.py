'''
    * 리스트 자료형
        - 리스트명 = [데이터, 데이터, 데이터,.....]
'''

# 데이터 없는 리스트
empty = []

# 데이터 있는 리스트
earPods = ["액티브 노이즈 캔슬링", "적응형 주변음 허용 모드", "터치 제어", "개인 맞춤형 공간 음향"]

# 데이터 조작하기
# 인덱스는 0부터 시작함
print(earPods[2])
print(earPods[-1])

# 데이터 추가하기
earPods.append("강한 생활 방수 디자인")
print(earPods)

earPods[1] = "기기 간 자동 전환"
print(earPods)

# 데이터 삭제하기
del earPods[0]
print(earPods)

# 리스트 슬라이싱
print(earPods[1:3])
print(earPods[:])
print(earPods[:4])
print(earPods[0:])

# 리스트 길이
print((len(earPods)))

# 리스트 정렬
earPods.sort()
print(earPods)