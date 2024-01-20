"""
Chapter 3
Python Advanced(3) - Meta Class(3)
Keyword - Type inheritance, Custom metaclass
"""
'''
메타클래스 상속
1. type 클래스 상속
2. meta class 속성 사용
3. 커스텀 메타 클래스 생성
   - 클래스 생성 가로채기(intercept)
   - 클래스 수정하기(modify)
   - 클래스 개선(기능추가)
   - 수정된 클래스 반환
'''

# Ex1
# 커스텀 메타클래스 생성 예제(type 상속 X)

def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d

def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new

# list를 상속 받음, 매소드 2개 추가
CustomList1 = type( 'CustomList1',
                    (list,),
                    {
                       'desc' :
                        '커스텀 리스트1',
                       'cus_mul': cus_mul,
                        'cus_replace' : cus_replace
                    }
                   )

c1 = CustomList1()
print('Ex1 >', c1)

# [1,2,3,4,5,6,7,8,9] -> self임
c1 = CustomList1([1,2,3,4,5,6,7,8,9])
print('Ex1 >', c1)

c1.cus_mul(1000)
print('Ex1 >', c1)
c1.cus_replace(1000, 7777)
print('Ex1 >', c1)
print('Ex1 >', c1.desc)
print('Ex1 >', dir(c1))

# Ex2
# 커스텀 메타클래스 생성 예제 (type 상속 O)

# class MetaClassName(type):
#     def __new__(metacls, name, bases, nemespace):
#         코드 작성

# new -> init -> call 의 실행 순서를 가짐
class CustomListMeta(type):

    # 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, dict):
        print('__init__ ->', self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict)

    # 인스턴스 실행
    def __call__(self, *args, **kwargs):
        print('__call__ ->', self, *args, **kwargs)
        return super().__call__(*args, **kwargs)

    # 클래스 인스턴스 생성 (메모리 초기화)
    def __new__(metacls, name, bases, namespace):
        print('__new__ ->', metacls, name, bases, namespace)
        namespace['desc'] = '커스텀 리스트2'
        namespace['cus_mul'] = cus_mul
        namespace['cus_replace'] = cus_replace

        return type.__new__(metacls, name, bases, namespace)

CustomList2 = CustomListMeta(
    'CustomList2',
    (list,),
    {}
)

# [1,2,3,4,5,6,7,8,9] -> self임
c2 = CustomList2([1,2,3,4,5,6,7,8,9])
print('Ex2 >', c2)

c2.cus_mul(1000)
print('Ex2 >', c2)
c2.cus_replace(1000, 7777)
print('Ex2 >', c2)
print('Ex2 >', c2.desc)
print('Ex2 >', dir(c2))

# 상속 확인
print(CustomList2.__mro__)