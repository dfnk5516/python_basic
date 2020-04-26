#Section04-3
#파이썬 데이터 타입(자료형)
#리스틀, 튜플

#리스트(순서o, 중복o, 수정o, 삭제o)
#선언

a=[]
b = list()
c = [1,2,3,4]
d = [10, 100, "Pen", "Banana", "Orange"]
e = [10, 100, ["Pen", "Banana", "Orange"]]

#인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])

#연산
print(c + d)
print(c * 3)
# print(c[0] + "hi") - error
print(str(c[0]) + "hi")

#리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1] #인덱스의 원소 제거
print(c)

print()
print()

#리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7)
print(y)
y.remove(2) #값일치 원소 제거
print(y)

y.pop() #제일 마지막거 꺼내기
print(y)
ex = [88, 77]
y.append(ex) #한꺼번에 넣기 [6, 5, 7, 4, 3, [88, 77]]
print(y)

y.extend(ex) #하나씩 넣기 [6, 5, 7, 4, 3, 88, 77]
print(y)

# 튜플(순서o, 중복o, 수정x, 삭제x)
a = ()
b = (1,)
c = (1,2,3,4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)
print()
print()

# 튜플 함수
z = (5, 2, 1, 3, 1)
print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))
