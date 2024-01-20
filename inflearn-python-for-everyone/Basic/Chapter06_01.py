# 파이썬 클래스
# OOP(객체지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 세상에 존재하는 모든 것을 클래스로 만들고 클래스를 객체로 구현하고 코드를 통해서 인스턴스화 시킴
# 구현할 대상을 인스턴스라고함
# 따라서 객체는 클래스와 인스턴스를 포함하는 개념

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할때 저장되는 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수: 객체마다 별도 존재

# 예제1
# class Dog(object): # object 상속받음
#     pass
class Dog: # 모든 클래스는 기본적으로 object를 상속받음
    # 클래스 속성
    spcies = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
coco = Dog("coco", 9)
chorong = Dog('chorong', 3)

# 비교
print(coco == chorong, id(coco), id(chorong))

# 네임스페이스
print('coco', coco.__dict__)
print('chorong', chorong.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(coco.name, coco.age, chorong.name, chorong.age))

if coco.spcies == 'firstdog':
    print('{} is {}'.format(coco.name, coco.age))

print(Dog.spcies)
print(coco.spcies)
print(chorong.spcies)

# 코드의 재사용성이 높아짐에 따라 생산성 향상

# 예제2
# self의 이해
# self는 인스턴스 그 자체를 의미함
class SelfTest:
    # self가 없기 때문에 클래스 메소드 (클래스로만 호출 가능)
    def func1():
        print('Func1 called')

    # self가 있끼 때문에 인스턴스 메소드 (인스턴스로만 호출 가능)
    def func2(self):
        print(self)
        print(id(self))
        print('Func2 calles')

f = SelfTest()

print(id(f))
# f.func1() # 에러 발생
f.func2()

# self가 없기 때문에 클래스로 바로 접근 가능
SelfTest.func1()
# self가 있기 때문에 클래스로 접근 불가능
# SelfTest.func2() # 에러 발생

# 예제3
# 클래스 변수, 인스턴스 변수
class WareHouse:
    # 클래스 변수 (공유하는 값)
    stock_num = 0

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Lee')
print(user1.stock_num)
user2 = WareHouse('Cho')

print(WareHouse.stock_num)
print(user1.stock_num)
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(print(WareHouse.__dict__))
user3 = WareHouse('Cho')
# 인ㅅ턴스의 네임스페이스에 없으면 클래스의 네임스페이스에 가서 값을 찾는다.
print(user2.stock_num)

print('befor', WareHouse.__dict__)
del user1
print('after', WareHouse.__dict__)

# 예제4
class Dog2: # 모든 클래스는 기본적으로 object를 상속받음
    # 클래스 속성
    spcies = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성
c = Dog2('july', 4)
d = Dog2('mery', 10)
# 메소드 호출
print(c.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('멍멍'))