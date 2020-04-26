#Section06
#python function & Lambda

#함수 정의 방법
#def 함수명(parameter):
#   code

#함수 호출
#함수명(parameter)

#함수 선언 위치 중요

#예제1
def hello(world):
    print("Hello", world)

hello("Python")
hello(7777)

def hello_return(world):
    val = "Hello " + str(world)
    return val

str1 = hello_return(333)
print(str1)

#다중 리턴
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(1)
print(val1, val2, val3)

def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3] #list 로 return

def func_mul3(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3) #tuple 로 return

#예제4
# *args, *kwargs

# *args 가변
#def args_func(*args):
#    print(args)

# def args_func(*args):
#    for t in args:
#        print(t)

# def args_func(*args):
#     for i, v in enumerate(args):
#         print(i, v)

def args_func(*args):
    for i, v in enumerate(range(10)):
        print(i, v)

args_func('kim')
args_func('kim', 'Park')
args_func('kim', 'Park', 'Lee')
