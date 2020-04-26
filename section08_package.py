from pkg.fibonacci import Fibonacci #여러개는 콤마로 구분

Fibonacci.fib(300)

print("ex2 : " , Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)  #인스턴스 생성후 호출

# 사용2(클래스) - 권장 x
#from pkg.fibonacci import *

#사용3(클래스)
from pkg.fibonacci import Fibonacci as fb
fb.fib(300)

print("ex2 : " , fb.fib2(400))
print("ex2 : ", fb().title)  #인스턴스 생성후 호출

#사용4(함수)
import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

#사용5(함수)
from pkg.calculations import div as d
print("ex5 : ", int(d(100, 10)))

#사용6
import pkg.prints as p
import builtins #파이썬 기본제공 패키지
p.prt1()
p.prt2()
print(dir(builtins))