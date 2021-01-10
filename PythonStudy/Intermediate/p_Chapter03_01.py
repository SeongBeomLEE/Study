# Special 메소드 == 매직 메소드 설명
# Special Method(Magic Method)
# 파이썬 데이터 모델
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(Built-in, 내부적으로 이미 만들어진) 메소드


# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(type(n))
print(n + 100)
print(n.__add__(100))
# print(n.__doc__)

print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

# 클래스 예제1
class Fruit():
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'F C Info : {} {}'.format(self._name, self._price)

    def __add__(self, x):
        print('Called __add__')
        return (self._price + x._price) * 0.8

    def __sub__(self, x):
        print('Called __sub__')
        return self._price - x._price

    def __le__(self, x):
        print('Called __le__')
        if self._price <= x._price: return True
        else: return False

    def __ge__(self, x):
        print('Called __ge__')
        if self._price >= x._price: return True
        else: return False

# 인스턴스 생성
s1 = Fruit('O', 7500)
s2 = Fruit('B', 3000)

# 매직메소드를 사용하지 않는 다면
print(s1._price + s2._price)

# 매직 메소드를 구현해서 이렇게 사용가능
print(s1 + s2)

# 매직메소드
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)

# import pandas as pd
# print((pd.DataFrame().__doc__))