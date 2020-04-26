#section04-4
#python data type(자료형)
#dictionary, set


#dictionary : 순서x, 중복x, 수정o, 삭제o
#key, value(Json) -> MongoDB
#선언
a = {'name' : 'choi', 'phone' : '010-5701-5517', 'birth' : 921221}
b = {0 : 'Hello Python', 1 : 'Hello Coding'}
c = {'arr' : [1, 2, 3, 4, 5]}

print(type(a))

#출력
print(a['name'])
#print(a['name1']) - error

print(a.get('name'))
print(a.get('name1'))

print(c['arr'][1:3])

#딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3)
print(a)

#key, values, items
#a = {'name' : 'choi'}
#key : name
#value : choi
#item : 'name' : 'choi'

print(a.keys())
#print(a.keys()[1]) - error
print(list(a.keys()))
print(list(a.keys())[1])
temp = list(a.keys())
print(temp[1:3])

print(a.values())

print(1 in b)
print(2 in b)
print('name2' not in a)

#집합(set)(순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)
print("i like python".replace("i like python","I love python"))

l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#교집합
print(s1.intersection(s2))
print(s1 & s2)

#합집합
print(s1 | s2)
print(s1.union(s2))

#차집합
print(s1 - s2)
print(s1.difference(s2))

#추가 & 제거
s3 = set([7, 8 , 10, 15])

s3.add(18)
#s3.add(7)
print(s3)
s3.remove(15)
print(s3)

print(type(s3))