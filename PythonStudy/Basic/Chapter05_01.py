# 파이썬 함수 및 중요성
# 파이썬 함수식 및 lambda

# 함수 정의 방법
# def function_name():
#     code

# 예제1
def firstFunc(w):
    print("Hello,", w)

firstFunc(3)

# 예제2
def returnFunc(w):
    value = "Hello, " + str(w)
    return value

x = returnFunc(3)
print(x)

# 예제3(다중반환)
def funcMul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = funcMul(2)
print(x, y, z)

# 튜플리턴
def funcMul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

t = funcMul(2)
print(type(t))

# 리스트리턴
def funcMul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

l = funcMul(2)
print(type(l))

# 딕셔너리 리턴
def funcMul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'y1' : y1, 'y2' : y2, 'y3' : y3}

d = funcMul(2)
print(type(d))

# 중요
# *args, **kwargs

# *args(언팩킹) -> 튜플 형태의 자료형
# 몇개가 오더라도 풀어서(언팩킹) 만들어줄게
# 가변인자를 사용할 수 있게 만들어줌
def argsFunc(*args):
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-'*10)

argsFunc('Lee')
argsFunc('Lee', 'Park')
argsFunc('Lee', 'Park','Kim')

# **kwargs(언팩킹) -> 딕셔너리 형태의 자료형
# 몇개가 오더라도 풀어서(언팩킹) 만들어줄게
# 가변인자를 사용할 수 있게 만들어줌
def kwargsFunc(**kwargs):
    for v in kwargs.keys():
        print('Result : {}'.format(v), kwargs[v])
    print('-'*10)

kwargsFunc(name1 = 'Lee')
kwargsFunc(name1 = 'Lee', name2 = 'Park')
kwargsFunc(name1 = 'Lee', name2 = 'Park', name3 = 'Kim')
kwargsFunc(sendSMS=False)

# 전체 혼합 아스타가 붙은 언팩킹 사용법
def example(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', arg1=20, arg2=30, arg3=40)

# 중첩함수
def nestedFunc(num):
    def nestedInFunc(num):
        print(num)
    print('In func')
    nestedInFunc(num + 100)

nestedFunc(100)
# nestedInFunc(100) # 에러 발생

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# 일반적 함수 할당
def mul_func(x, y):
    return x * y

# 람다 함수 할당
a = lambda x, y : x * y

print(mul_func(1,2))

mul_func_var = mul_func
print(mul_func_var(1,2))

print(a(1,2))

def func_final(x, y, func):
    print(x * y * func(10, 10))

func_final(10,10, lambda x, y : x*y)
func_final(10,10, mul_func)