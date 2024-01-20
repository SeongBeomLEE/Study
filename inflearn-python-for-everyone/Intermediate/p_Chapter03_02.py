# Special 메소드 == 매직 메소드 설명
# Special Method(Magic Method)
# 파이썬 데이터 모델
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(Built-in, 내부적으로 이미 만들어진) 메소드

# 클래스 예제2
# 백터(x,y)를 계산하는 클래스
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# max((5,10)) -> 10

class Vector():
    def __init__(self, *args):
        '''
        Create a vector, example : v = Vector(5, 10)
        '''
        if len(args) == 0: self._x, self._y = 0, 0
        else: self._x, self._y = args

    def __repr__(self):
        '''Return the vector information'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Return the vector add'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        '''Return the vector mul'''
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        '''Return the vector mul'''
        # 0,0 인지를 확인하는 메소드
        return bool(max(self._x, self._y))

# Vector 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector()

# 매직메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v1 * 5)
print(bool(v1), bool(v2), bool(v3))

