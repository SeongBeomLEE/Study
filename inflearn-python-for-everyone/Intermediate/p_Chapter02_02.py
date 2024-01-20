# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지 보수 쉬움, 대형프로젝트에 적합
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    # 코멘트
    """
    Car class
    Author : Lee
    Date:2020.12.29
    사용법 : .....
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    car_count = 0


    def __init__(self, company, details):
        self._company = company
        self._details = details
        self.car_count = 10
        Car.car_count += 1

    # 이미 파이썬에서 구현된 메소드 # 매직 메소드
    def __str__(self): # 사용자 레벨에서
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): # 개발자 레벨에서 (객체 정보까지 문자로 표현해줌)
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        print('호출 가능?')
        Car.car_count -= 1

    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))


# self 의미 (인스턴스 내부의 예약어)
car1 = Car('F', {'color': 'White', 'hor': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'hor': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'hor': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))

print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(Car.__doc__)

car1.detail_info()
Car.detail_info(car1)
car2.detail_info()
Car.detail_info(car2)

# 에러
# Car.detail_info() # 'self' 가 없기 때문에 에러 발생

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))
print(car1.__class__ == car2.__class__) # 같은 부모를 쓰기 때문에

# 공유 확인

print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)

# 삭제 확인
del car2

print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스))
