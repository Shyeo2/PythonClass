'''
    1. Dictionary
        - 시퀀스 자료형
        - 사전형태의 자료형
        - 키와 데이터를 가지고 있는 사전형 자료형
        - 사전형태의 자료를 만들때 편리

        Dictionary = {키1: 데이터1 , 키2: 데이터2}

    2. Dictionary 접근하기
        Dictionary ["키"]

        Dictionary 할당하기
        Dictionary["키"] = 데이터

        Dictionary 삭제하기
        del Dictionary["키"]

'''

# Dictionary 만들기
stock_a = {"삼성전자" : 61000 , "LG전자" : 90400}

stock_b = {
    "삼성전자" : [61000, 61500, 62000, 62500, 62000],
    "LG전자" : (90400, 90900, 90300, 90500, 9000)
}

stock_c = {
    "삼성전자" : {
        "현재가" : 61000,
        "보유수량" : 10,
        "매수단가" : 60000
    }
}

print(stock_a)
print(stock_b)
print(stock_c)

# Dictionary 접근하기
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

# Dictionary 할당하기
stock_a["삼성전자"] = 65000
print(stock_a)

# Dictionary 삭제하기
del stock_a["LG전자"]
print(stock_a)

# Dictionary 함수
stock_d = {
    "삼성전자" : 61000,
    "sk하이닉스" : 86100,
    "NAVER" : 186000,
    "카카오" : 57100
}

# items() : 키와 데이터 쌍
for item in stock_d.items():
    print(item)

# keys() : 키
for key in stock_d.keys():
    print(key)

# values() : 데이터
for value in stock_d.values():
    print(value)










