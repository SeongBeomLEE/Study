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
    Descriprion : Class, Static, Instance Method
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    price_per_raise = 1.0
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 이미 파이썬에서 구현된 메소드 # 매직 메소드
    def __str__(self): # 사용자 레벨에서
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): # 개발자 레벨에서 (객체 정보까지 문자로 표현해줌)
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def get_price(self):
        return 'Before Car price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car price -> company : {}, price : {}'.format(self._company, self._details.get('price')*Car.price_per_raise)

    # Class Method
    # cls가 곧 class
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed ! Price increased')

    # Static Method
    # 기본적으로 받아야할 인자가 존재하지 않음
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return "Ok! This is {}".format(inst._company)
        else:
            return "No! This is {}".format(inst._company)


# self 의미 (인스턴스 내부의 예약어)
car1 = Car('F', {'color': 'White', 'hor': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'hor': 270, 'price': 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보 (직접 접근)
# 이러한 접근 방법은 좋지 않음
print(car1._details.get('price'))
print(car2._details.get('price'))

# 가격정보 (인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격정보 (인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)

# 가격정보 (인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 인스턴스로 호출
print(car1.is_bmw(car1))
print(car1.is_bmw(car2))

# 클래스로 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))