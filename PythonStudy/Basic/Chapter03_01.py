# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열 (시퀀스)
list : 리스트 (시퀀스)
tuple : 튜플 (시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
_bool = True
str2 = 'Anaconda'
_float = 10.0
print(_float == 10)
# 데이터 타입은 다르다는 것을 알 수 있음
print(type(_float) == type(10))
_int = 7
_list = [str1, str2]
#       key 값, value 값
_dict = {'name' : 'ML',
        'version' : 2.0}
print(_dict.keys())
print(_dict.values())
print(_dict.items())
print(_dict['name'])

# tuple1과 tuple2는 같은 것
_tuple1 = (7, 8, 9)
_tuple2 = 7, 8, 9
_set = {3, 5, 7}

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) == x**y
"""

# 정수 선언
i = 77
j = -14
big_i = 7777777777777777777777

# 정수 출력
print(i)
print(j)
print(big_i)

# 실수 출려
f = 0.99
f2 = 3/9
print(f)
print(f2)

# 연산 실습
i1 = 39
i2 = 939
big_i1 = 1111111111111111111
big_i2 = 3333333333333333333
f1 = 1.121
f2 = 1.213

print(i1 + i2)
print(i1 - i2)
print(i1 * i2)
print(i1 / i2)
print(i1 // i2)
print(i1 % i2)
print(i1**2)
print(pow(i1, 2))

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

print(type(a), type(b), type(c), type(d))
print(float(b))
print(int(d))
print(complex(7))

print(abs(-7))
# 몫과 나머지
x, y = divmod(100, 8)
print(x, y)
print(pow(x, y))

# 외부 모듈
import math
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)

import scipy as sp
import numpy as np