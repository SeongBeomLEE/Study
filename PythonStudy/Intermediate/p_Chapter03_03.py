# Special 메소드 == 매직 메소드 설명
# Special Method(Magic Method)
# 파이썬 데이터 모델
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(Built-in, 내부적으로 이미 만들어진) 메소드

# 객체 -> 파이썬의 데이터를 추상화(사용할 수 있게 만든다)
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
l_leng1 = ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5
print(l_leng1)

# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)
print(pt4)
print(pt3[0])
print(pt4[0])
print(pt3.x)
print(pt4.x)

l_leng2 = ((pt3.x - pt4.x)**2 + (pt3.y - pt4.y)**2)**0.5
print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default = False

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to unpacking
# * -> 튜플, **-> 딕셔너리
temp_dict = {'x':75, 'y':55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

print(p1)
print(p2)
print(p3)
# rename test
print(p4)
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

# Unpacking
x, y = p3
print(x, y)

# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 리스트를 기반으로 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)

# _fields: 필드 네임 확인
print(p1._fields, p2._fields, p3._fields, p4._fields)

# _asdict() : OrderedDict 반환
print(p1._asdict())
print(p4._asdict())

# 실사용 실습
# 한반에 20명, 4개의 반(A, B, C, D)
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()
print(numbers)
print(ranks)

# List Comprehention
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

# 추천
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                for number in [str(n) for n in range(1,21)]]

print(len(students2))
print(students2)

# 출력
for s in students:
    print(s)
