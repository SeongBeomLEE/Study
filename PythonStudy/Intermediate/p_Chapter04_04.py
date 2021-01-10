# Sequence - 시퀀스
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict

# 읽기 전용의 딕셔너리를 만들 수 있음 (수정이 불가함)
from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only
d_forzen = MappingProxyType(d)

print(d, id(d))
print(d_forzen, id(d_forzen))

print('-'*50)

# 수정 불가
# d_forzen['key2'] = 'value2'

# 수정 가능
d['key2'] = 'values2'
print(d)

print('-'*50)

# Set

s1 = {'A', 'O', 'A', 'O', 'K'}
s2 = set(['A', 'O', 'A', 'O', 'K'])
s3 = {3}
s4 = {} # 딕셔너리 타입이 됨
print(type(s4))
s5 = set() # 공백
s6 = frozenset({'A', 'O', 'A', 'O', 'K'})# 값이 추가가 안됨 (읽기 전용)

s1.add('M')
print(s1)

# 추가 불가
# s6.add('M')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))
print(s6, type(s6))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis
print('-------')
print(dis('{10}'))
print('-------')
print(dis('set([10])'))

# 지능형 집합(comprehending set)
print('-----')
from unicodedata import name
print({name(chr(i), '') for i in range(0,256)})