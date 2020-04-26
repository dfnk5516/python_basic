class UserInfo:
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)


user1 = UserInfo("Kim")

user1.user_info_p()

print(user1.name)
print(id(user1))
print(user1.__dict__)



class SelfTest():
    @staticmethod
    def function1():
        print('function1 called!')

    def function2(self):
        print(id(self))
        print('function2 called!')

self_test = SelfTest()
#self_test.function1()
SelfTest.function1() #class method - static 같은거인듯
self_test.function2() #인스턴스 method

print(id(self_test))
SelfTest.function2(self_test)

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self): #소멸자
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) #자기 인스턴스에 없으면 클래스 변수에서 찾음 

del user1
print(WareHouse.stock_num)