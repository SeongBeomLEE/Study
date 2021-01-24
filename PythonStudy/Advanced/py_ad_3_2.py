"""
Chapter 3
Python Advanced(3) - Meta Class(2)
Keyword - Type(name, base, dct), Dynamic metaclass
"""

'''
메타 클래스
1. 메타 클래스 동적 생성 중요
2. 동적 생성한 메타 클래스 -> 커스텀 메타클래스 생성(우리가 의도하는 대로 클래스를 만드는 것)
3. 의도하는 방향으로 직접 클래스 생성에 관여할 수 있는 큰 장점
'''

# Ex1
# type 동적 클래스 생성 예제
n = 10
print(type(n))
# Name(이름), Basses(상속), Dct(속성, 메소드)

# 밑에와 동일항 방식
class Sample1():
    pass

s1 = type('Sample1', (), {})

print('Ex1 >', s1)
print('Ex1 >', type(s1))
print('Ex1 >', s1.__base__) # 모든 클래스는 object를 상속 받기 때문에
print('Ex1 >', s1.__dict__)

# 동적 셍성 + 상속
class Parent1():
    pass

class Sample2(Parent1):
    attr1 = 100
    attr2 = 'hi'

# 클래스를 동적으로 만듬
s2 = type(
    'Sample2',
    (Parent1,),
    dict(attr1 = 100, attr2 = 'hi')) # {'attr1' : 100, 'arrt2' : 'hi'}

print('Ex2 >', s2)
print('Ex2 >', type(s2))
print('Ex2 >', s2.__base__)
print('Ex2 >', s2.__dict__)
print('Ex2 >', s2.attr1, s2.attr2)

print()

# Ex2
# type 동적 클래스 생성 + 메소드

class SampleEx:
    attr1 = 30
    attr2 = 100

    def add(self, m ,n):
        return m + n

    def mul(self, m, n):
        return m * n

ex = SampleEx()

print('Ex2 >', ex.attr1)
print('Ex2 >', ex.attr2)
print('Ex2 >', ex.add(100, 200))
print('Ex2 >', ex.mul(100, 20))

print()
# 동적 클래스 생성
s3 = type(
    'Sample3',
    (object, ),
    dict(attr1 = 300, attr2 = 1000,
         add = lambda x, y : x + y, mul = lambda x, y : x * y))
# {'attr1' : 30, 'attr2' : 100, 'add' : lambda x, y : x + y, 'mul' : lambda x, y : x * y}

print('Ex2 >', s3.attr1)
print('Ex2 >', s3.attr2)
print('Ex2 >', s3.add(100, 200))
print('Ex2 >', s3.mul(100, 20))
