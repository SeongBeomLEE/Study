# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지 보수 쉬움, 대형프로젝트에 적합
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩
# 차량1
car_company_1 = 'F'
car_detail_1 = [
    {'color' : 'White'},
    {'hor' : 400},
    {'price' : 8000}
]

# 차량2
car_company_2 = 'BMW'
car_detail_2 = [
    {'color' : 'Black'},
    {'hor' : 270},
    {'price' : 5000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color' : 'Silver'},
    {'hor' : 300},
    {'price' : 6000}
]

# 리스트 구조
# 관리하기 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['F', 'BMW', 'Audi']
car_detail_list = [
    {'color': 'White', 'hor': 400, 'price': 8000},
    {'color': 'Black', 'hor': 270, 'price': 5000},
    {'color': 'Silver', 'hor': 300, 'price': 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print('-'*30)

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

car_dicts = [
    {'car_company':'F', 'car_detail':{'color': 'White', 'hor': 400, 'price': 8000}},
    {'car_company':'BMW', 'car_detail':{'color': 'Black', 'hor': 270, 'price': 5000}},
    {'car_company':'Audi', 'car_detail':{'color': 'Silver', 'hor': 300, 'price': 6000}}
]

del car_dicts[1]
print(car_dicts)

print('-'*30)

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 이미 파이썬에서 구현된 메소드 # 매직 메소드
    def __str__(self): # 사용자 레벨에서
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): # 개발자 레벨에서 (객체 정보까지 문자로 표현해줌)
        return 'repr : {} - {}'.format(self._company, self._details)

car1 = Car('F', {'color': 'White', 'hor': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'hor': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'hor': 300, 'price': 6000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print(dir(car1))

print('-'*30)

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# 리스트 안에서 반환할 때는 repr이 사용됨
print(car_list)
print('-'*30)

for x in car_list:
    print(x)
    print(repr(x))
