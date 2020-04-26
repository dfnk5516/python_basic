#읽기 모드 r, 쓰기모드(기존 파일 삭제) w, 추가모드(없으면 생성, 있으면 뒤에 추가) a
# https://docs.python.org/3.7/library/functions.html#open
# if False:
#     print("No")
# else:
#     print("Yes")

# print(1 and True)
# print(0 or True)

score = 80

# if score >= 90:
#     print(1)
# elif score >= 80:
#     print(2)
# elif score >= 70:
#     print(3)
# elif score >= 60:
#     print(4)

# numbers = []
# for n in range(1, 100 + 1):
#     if n % 2 ==0:
#         numbers.append(n)



# numbers = [n for n in range(1, 100+1) if n % 2 == 0]

# print(numbers)

before_numbers = range(1, 100 + 1)
numbers = list(filter(lambda n: n%2==0, before_numbers))
print(numbers)

name = "김패캠"
try:
    float(name)
except ValueError:
    print("2번 에러")
except SyntaxError:
    print("3번 에러")
except Exception:
    print("1번 에러")
else:
    print("else")