# 집합(Set) 특징
# 집합 자료형 (순서X, 중복X, 추가O, 삭제O)

# 선언
a = set()
print(type(a), a)

b= set([1,2,3,4,5,6,7,8,9,1])
print(type(b), b)

c = set([4,2,3,4,'s','f'])
print(type(c), c)

d = {1,2,3,4,'fgfg','sdfds'}
print(type(d), d)

e = {1,2,32,(1,23,43),(2,32442,34)}
print(type(e), e)

# 튜플 변환
t = tuple(b)
print(type(t), t)

# 리스트 변환
l = list(b)
print(type(l), l)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))

# 집합 자료형 활용
s1 = set([1,2,3,4,5,6,7])
s2 = set([4,5,6,7,8,9,10])
# 교집합
print('s1 & s2:', s1 & s2)
print('s1.intersection(s2):', s1.intersection(s2))
#합집합
print('s1 | s2:', s1 | s2)
print('s1.union(s2):', s1.union(s2))
#차집합
print('s1 - s2:', s1 - s2)
print('s1.difference(s2):', s1.difference(s2))

# 중복 원소 확인
print(s1.isdisjoint(s2)) # 교집합이면 False

# 부분 집합 확인
# s1이 가로 함수에 부분집합이냐
print(s1.issubset([1,2,3,4,5,6,7,8]))
# 가로가 s1의 부분집합이냐
print(s1.issuperset([1,2,3,4,5,6,7,8]))

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print(s1)

# 없는 원소를 삭제하려고 하며 에러 발생
s1.remove(2)
print(s1)

# 없는 원소를 삭제하려고 하며 에러를 발생하지 않음
s1.discard(2)
print(s1)

s1.clear()
print(s1)