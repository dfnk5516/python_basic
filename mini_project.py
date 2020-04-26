import sqlite3
import os
import platform

conn = ''


class Item:
    def __init__(self, code, name, price):
        self.code  = code
        self.name = name
        self.price = price

        if code[0].upper() == 'A':
            self.classify = '수산'
        elif code[0].upper() == 'B':
            self.classify = '과일'
        elif code[0].upper() == 'C':
            self.classify = '유제품'

class CartItem(Item):
    def __init__(self, code, name, price, quantity):
        super(CartItem, self).__init__(code, name, price)
        self.quantity = quantity

class Cart:
    #__cartList = [CartItem('aa','aa', 3, 5), CartItem('bb','bb', 4, 6)]
    __cartList = []
    
    @staticmethod
    def setCartList(cartList):
        Cart.__cartList = cartList
    @staticmethod
    def getCartList():
        return Cart.__cartList

class MyError(Exception):
    def __init__(self, message):
        super().__init__(message)
    


def init():
    try:
        if not(os.path.isdir('D:/python_basic/resource')):
            os.makedirs(os.path.join('D:/python_basic/resource'))
            
    except OSError as e:
        print(e)
    finally:
        conn = sqlite3.connect('D:/python_basic/resource/brian.db', isolation_level=None)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS items(code text PRIMARY KEY, name text, price integer, classify text)")
        conn.execute("delete from items").rowcount
        c.execute("CREATE TABLE IF NOT EXISTS cart(code text PRIMARY KEY, name text, price integer, classify text, quantity integer)")

        c = conn.cursor()
        c.execute('SELECT * FROM cart')
        cartItem = c.fetchall()
        temp = []
        #print(cartItem)
        for v in cartItem:
            temp.append(CartItem(v[0], v[1], v[2], v[4]))
        
        Cart.setCartList(temp)


        itemList = (
            ('A01', '새우', 1000),
            ('A02', '상어', 15000),
            ('A03', '거북', 10000),
            ('B01', '사과', 1500),
            ('B02', '모과', 2000),
            ('B03', '자두', 3000),
            ('C01', '우유', 2000),
            ('C02', '버터', 3000),
            ('C03', '두유', 4000)
        )

        li = []
        for v in itemList:
            #print(v[0])
            li.append(Item(v[0],v[1],v[2]))

        for v in li:
            c.execute("INSERT INTO items(code, name, price, classify) VALUES (?, ?, ?, ?)", (v.code, v.name, v.price, v.classify))


# 메뉴 출력
def prt_cart():
    cartList = Cart.getCartList()
    index = 0
    if platform.system() == 'Windows':
            os.system('cls')
    else:
        os.system('clear')
    print("******************************************")
    print("*     welcome to the fastCampusMart!!    *")
    print("******************************************")
    if len(cartList) != 0:
        print("[나의 장바구니]")
    for v in cartList:
        index = index + 1
        print('색인 : {}, 상품명 : {}, 수량 : {}, 가격 : {}'.format(index, v.name, v.quantity, v.price))

def prt_menu():
    
    while True:
        prt_cart()
        #print(index, v.code)

        print("1. 장보기")
        print("X. 장바구니 관리 - 미구현")
        print("3. 쉬고 나중에 마저 장보기")
        print("4. 계산하고 나가기")

        menu = 0
        # 메뉴 넘버 입력
        try:
            menu = int(input("Select Menu Number : "))
            if menu != 2 and menu > 0 and menu < 5:
                break
            else:
                raise MyError('올바른 번호를 입력하시오 ...')
        except ValueError:
            print('올바른 번호를 입력하시오 ...')
        except MyError as e:
            print(e)
    return menu

def prt_shop():
    while True:
        prt_cart()
        print("1.수산시장")
        print("2.과일시장")
        print("3.유제품시장")

        menu = 0
        try:
            menu = int(input("Select Menu Number : "))
            if menu > 0 and menu < 4:
                break
            else:
                raise MyError('올바른 번호를 입력하시오 ...')
        except ValueError:
            print('올바른 번호를 입력하시오 ...')
        except MyError as e:
            print(e)
    return menu


def prt_fish():
    level = 0
    conn = sqlite3.connect('D:/python_basic/resource/brian.db', isolation_level=None)
    c = conn.cursor()
    param = ('수산',)
    c.execute("SELECT * FROM items where classify=?", param) # Item 클래스가 들어있는 자료구조로 받아오고 싶은데 시간부족으로 방법을 못찾았습니다 가능하다면 이 부분 피드백 부탁드립니다

    item = c.fetchall()
    #print(item)

    while True:
        index = 0
        prt_cart()
        for v in item:
            index = index + 1
            print("{}. {} {}원".format(index, v[1], v[2]))

        menu = 0
        name = ''
        
        if level == 0:
            print('무엇을 사시겠습니까')
            try:
                menu = int(input("Select item Number : "))
                if menu > 0 and menu < 4:
                    level = 1
                    name = item[menu - 1][1]
                else:
                    raise MyError('올바른 번호를 입력하시오 ...')
            except ValueError:
                print('올바른 번호를 입력하시오 ...')
            except MyError as e:
                print(e)
        quantity = 0

        if level == 1:
            print('{} 몇 마리를 사시겠습니까'.format(name))
            try:
                quantity = int(input("Select quantity : "))
                break
            except ValueError:
                print('올바른 번호를 입력하시오 ...')
    return CartItem(item[menu - 1][0], item[menu - 1][1], item[menu - 1][2], quantity)

   

def prt_fruit():
    level = 0
    conn = sqlite3.connect('D:/python_basic/resource/brian.db', isolation_level=None)
    c = conn.cursor()
    param = ('과일',)
    c.execute("SELECT * FROM items where classify=?", param)

    item = c.fetchall()
    #print(item)

    while True:
        index = 0
        prt_cart()
        for v in item:
            index = index + 1
            print("{}. {} {}원".format(index, v[1], v[2]))

        menu = 0
        name = ''
        
        if level == 0:
            print('무엇을 사시겠습니까')
            try:
                menu = int(input("Select item Number : "))
                if menu > 0 and menu < 4:
                    level = 1
                    name = item[menu - 1][1]
                else:
                    raise MyError('올바른 번호를 입력하시오 ...')
            except ValueError:
                print('올바른 번호를 입력하시오 ...')
            except MyError as e:
                print(e)
        quantity = 0

        if level == 1:
            print('{} 몇 개를 사시겠습니까'.format(name))
            try:
                quantity = int(input("Select quantity : "))
                break
            except ValueError:
                print('올바른 번호를 입력하시오 ...')
    return CartItem(item[menu - 1][0], item[menu - 1][1], item[menu - 1][2], quantity)

def prt_dairy():
    level = 0
    conn = sqlite3.connect('D:/python_basic/resource/brian.db', isolation_level=None)
    c = conn.cursor()
    param = ('유제품',)
    c.execute("SELECT * FROM items where classify=?", param)

    item = c.fetchall()
    #print(item)

    while True:
        index = 0
        prt_cart()
        for v in item:
            index = index + 1
            print("{}. {} {}원".format(index, v[1], v[2]))

        menu = 0
        name = ''
        
        if level == 0:
            print('무엇을 사시겠습니까')
            try:
                menu = int(input("Select item Number : "))
                if menu > 0 and menu < 4:
                    level = 1
                    name = item[menu - 1][1]
                else:
                    raise MyError('올바른 번호를 입력하시오 ...')
            except ValueError:
                print('올바른 번호를 입력하시오 ...')
            except MyError as e:
                print(e)
        quantity = 0

        if level == 1:
            print('{} 몇 개를 사시겠습니까'.format(name))
            try:
                quantity = int(input("Select quantity : "))
                break
            except ValueError:
                print('올바른 번호를 입력하시오 ...')
    return CartItem(item[menu - 1][0], item[menu - 1][1], item[menu - 1][2], quantity)
    

def add_cart(item):
    print(item)
    conn = sqlite3.connect('D:/python_basic/resource/brian.db', isolation_level=None)
    c = conn.cursor()
    param = (item.code,)
    c.execute("SELECT * FROM cart where code=?", param)

    if len(c.fetchall()) != 0:
        param = (item.quantity, item.code)
        c.execute("Update cart set quantity=? where code=?", param)
    else:
        param = (item.quantity, item.code, item.name, item.price, item.classify)
        c.execute("Insert into cart(quantity, code, name, price, classify) values (?, ?, ?, ?, ?)", param)
    
    cartItem = Cart.getCartList()
    check = False
    for v in cartItem:
        if v.code == item.code:
            check = True
            v.quantity = item.quantity
            break
    if check == True:
        return
    Cart.setCartList(Cart.getCartList().append(CartItem(item.code, item.name, item.price, item.quantity)))
    
    # check = False
    
    # for v in Cart.getCartList():
    #     if v.code == item.code:
    #         check = True
    #         v.quantity = item.quantity
    #         break
    # if check == True:
    #     return
    # Cart.setCartList(Cart.getCartList.append((item.code, item.quantity)))
        

    

def calculate():
    result = 0 
    for v in Cart.getCartList():
        result = result + (v.quantity * v.price)
    print('Thank you sir. Your total price is {}'.format(result))

    conn = sqlite3.connect('D:/python_basic/resource/brian.db', isolation_level=None)
    conn.execute("delete from cart").rowcount


   


# 프로그램 시작
def main():
    shopping = True
    while shopping:
        init()
        while True:
            page = prt_menu()
            if page == 1: # 장보기
                page = prt_shop()
                if page == 1: # 수산시장
                    add_cart(prt_fish())
                elif page == 2: # 과일시장 
                    add_cart(prt_fruit())
                elif page == 3: # 유제품시장
                    add_cart(prt_dairy())
            #elif page == 2: # 장바구니 관리
            elif page == 3: # 쉬고 나중에 마저 장보기
                shopping = False
                break
            elif page == 4: # 계산하고 나가기
                calculate()
                shopping = False
                break
    

    
    




if __name__ == "__main__":
    main()



# ## 데이터베이스를 연결하는 코드
# # conn = sqlite3.connect ...
# # c = conn.cursor()

# ## 상품과 주문 테이블을 생성하는 코드
# # c.execute("CREATE TABLE ...

# ## 상품 데이터를 추가하는 코드
# # c.execute("INSERT INTO ...

# ## 상품 목록을 표시하는 코드

# print('')
# print("구매하실 상품의 번호를 입력해주세요: ")


# ## 상품 번호와 주문 수량을 입력받는 코드
# print('')
# print("구매할 수량을 입력해주세요: ")


# ## 주문 데이터를 db에 추가하는 코드
# # c.execute("INSERT INTO ...

# ## 현재까지 주문 내역을 출력하는 코드
# print('')
# print("현재까지 구매한 내역 보기")
# print('')