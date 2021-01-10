# Chapter04-3
# 파이썬 반복문
# While 실습

# while <expr>:
#    <statement(s)>

# 예제1
n = 5
while n > 0:
    print(n) # 5 ~ 1 까지 출력
    n = n - 1

# 예제2
a = ['foo', 'bar', 'baz']

while a: # a를 역순으로 출력
    print(a.pop())

# if 중첩
# 예제3
# break , continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n) # 4 ~ 3 까지 출력
print('Loop Ended.')
print()

# 예제4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m) # 2를 제외하고 4 ~ 0까지 다 출력
print('Loop Ended.')

# 예제5
i = 1
while i <= 10:
    print('i:', i) # 1 ~ 6 까지 출력
    if i == 6:
        break
    i += 1

# While - else 구문

# 예제6
n = 10
while n > 0:
    n -= 1
    print(n) # 9 ~ 5 까지 출력
    if n == 5:
        break
else:
    print('else out.') # 중간에 brake문을 만났기 때문에 출력 X

# 예제6
n = 3
while n > 0:
    n -= 1
    print(n) # 2 ~ 0 까지 출력
else:
    print('else out.') # break문을 안만났기 때문에 출력

# 예제7
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'
i = 0
while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list.') # break를 만났기 때문에 출력X

# 무한반복
# while True:
#     print('Foo')

# 예제8
a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break # a가 []가 되면 반복문을 종료
    print(a.pop())