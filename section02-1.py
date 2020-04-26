# Section02-1
# python basic coding
# print

# basic output
print('Hello Python')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')

print()
#forman 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))
print("{0} , {1} and {0}".format("You", "Me"))
print("{a} and {b}".format(a="You", b="Me"))

print("%s's favorite number is %d" %("Tiger", 8))

print("Test1 : %5d, Price : %4.2f" %(776, 6534.123))
print("Test1 : {0: 5d}, Price :{1: 4.2f}".format(776, 6534.123) )
print("Test1 : {a: 5d}, Price :{b: 4.2f}".format(a=776, b=6534.1232))

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴 
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""

print('\'You\'')