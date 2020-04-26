# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
            "name" : "Kim",
            "age" : 25
         }

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9} 

print(type(v_tuple))
print(type(v_set))
print(type(v_float))

i1 = 39
i2 = 939
big_int1 = 99999999999999999999999999999999999
big_int2 = 77777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5 #0.5
f4 = 10. #10.0

import math
print(math.ceil(5.1)) #6
print(math.floor(3.874)) #3

a = 'niceman'
b='orange'
print(list(reversed(b)))
print(a[0:3]) #0~2 까지 나옴
print(a[0:len(a)])
print(a[:])
print(b[0:4:2]) # o, a / 0, 2
print(b[1:-2])
print(b[::-1])



print("i like python".capitalize().replace("like","love"))
print("i like python".replace("like","love").capitalize())
print("i like python".replace("i like python", "I love python"))