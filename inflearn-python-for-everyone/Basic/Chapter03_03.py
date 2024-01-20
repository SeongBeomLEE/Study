# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 파이썬 배열 제공X
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f  = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

# 인덱싱
print('>>>>>>')
print('type(d), d:', type(d), d)
print('d[1]:', d[1])
print('d[0] + d[1] + d[1]:', d[0] + d[1] + d[1])
print('d[-1]:', d[-1])
print('e[-1][1]:', e[-1][1])
print('list(e[-1][1]):', list(e[-1][1]))

# 슬라이싱
print('>>>>>>')
print('d[0:3]:', d[0:3])
print('d[2:]:', d[2:])
print('e[2][1:3]', e[2][1:3])

# 리스트 연산
print('>>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# 같은 id 값
temp = c
print(c == temp)
print(id(c), id(temp))


# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4
print('c[0] = 4:', c)
c[1:2] = ['a', 'b', 'c']
print("c[1:2] = ['a', 'b', 'c']:", c)
c[1] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print("c[1] = ['a', 'b', 'c']:", c)
c[1:3] = [] # 삭제
print('c[1:3] = []:', c)
del c[3]
print('del c[3]:', c)

# 리스트 함수
a = [5, 2, 3, 1, 4, 1, 1, 1, 1]

print('a - ', a)
a.append(6)
print('a.append(6):', a)
a.sort()
print('a.sort():', a)
a.reverse()
print('a.reverse():', a)
print('a.index(5):', a.index(5))
a.insert(2, 7)
print('a.insert(2, 7):', a)
a.reverse()
a.remove(1)
print('a.reverse() / a.remove(1):', a)
print('a.pop():', a.pop())
print('a.pop():', a.pop())
print('a - ', a)
print('a.count(4):', a.count(4))
ex = [8, 9]
a.extend(ex)
print('a.extend(ex):', a)

# 삭제 remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data, 2 is data)