class Monster:
    def say(self):
        print("안녕안녕~ 난 몬스터야:)")

mon = Monster()
mon.say()           #안녕안녕~ 난 몬스터야:)

print(type(mon))    #<class '__main__.Monster'>

a = 10
print(type(a))      #<class 'int'>

b = "문자열객체"
print(type(b))      #<class 'str'>
print(b.__dir__())
