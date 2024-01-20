# 파이썬 튜플
# 튜플 자료형(순서O, 중복O, 수정X, 삭제X) # 불변

# 선언
a = ()
b = (1,) # tuple 형
c = (1) # int 형
d = (1, 2, 3)
e = (1, 2, 3, ("A", "b", "c"))
print(type(a), type(b), type(c), type(d))

# 인덱싱
print(">>>>>>>>>")
print('d[1]:', d[1])
print('d[0] + d[1] + d[2]:', d[0] + d[1] + d[2])
print('list(e[-1]):', list(e[-1]))

# 수정X
# d[0] = 2

# 슬라이싱
print(">>>>>>>>>")
print('d[0:2]:', d[0:2])

# 튜플 연산
print('d+e:', d+e)

# 튜플 함수
a = (5,4,2,1,3)
print(a)
print(a.index(5))
print(a.count(5))

# 팩킹 & 언팩킹 (packing, unpacking
# 팩킹 - 하나로 묶다
t = ('foo', 'bar', 'baz', 'qux')
print(t)

# 언팩킹 - 각각 할당한다
(x1, x2 ,x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2 ,x3, x4)

t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6
print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)