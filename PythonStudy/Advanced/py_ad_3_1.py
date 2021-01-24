"""
Chapter 3
Python Advanced(3) - Meta Class(1)
Keyword - Class of Class, Type, Meta Class, Custom Meta Class
"""
'''
메타 클래스
1. 클래스를 만드는 역할 -> 의도하는 방향으로 클래스를 커스텀하는 것
2. 프레임워크(파이토치, 텐서플로우, 케라스, 장고 등) 작성 시 필수
3. 동적 생성(type), 커스텀 생성(type) 함수
4. 커스텀 클래스 -> 검증 클래스 등
5. 엄격한 CLass 사용 요구, 메소드 오버라이드 요구
'''

# Ex1
# type 예제
class SampleA(): # Class == object
    pass

# 클래스를 인스턴스화 했다.
obj1 = SampleA() # 변수에 할당, 복사 가능, 새로운 속성 추가 가능, 함수의 인자로 넘기기 가능
print('Ex1 >', obj1.__class__.__name__)

# obj1 -> SampleA instance
# SampleA -> type meta class
# type -> type meta class
print('Ex1 >', obj1.__class__)
print('Ex1 >', type(obj1))
print('Ex1 >', obj1.__class__ is type(obj1))

# 모든 클래스의 원형은 type(메타 클래스다)이다.
print('Ex1 >', obj1.__class__.__class__ is type(obj1).__class__)

print(type.__class__) # 핵심

# Ex2
# type mete(Ex1 증명)

# int, dict
n = 10 # 클래스임
d = {'a' : 10, 'd': 20} # 클래스임

class SampleB():
    pass

obj2 = SampleB()

for o in (n, d, obj2):
    print(f'Ex 2 > {type(o)} {type(o) is o.__class__} {o.__class__.__class__}')

print()

for t in int, float, list, tuple:
    print('Ex2 >', type(t))

print('EX2 >', type(type))