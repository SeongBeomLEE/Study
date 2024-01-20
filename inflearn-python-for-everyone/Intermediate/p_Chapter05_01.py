# 일급 함수 (일급 객체) -> 함수형 프로그래밍이 가능해짐
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# 함수 객체

def factorial(n):
    '''
    Factorial Funtion
    :param n: Int
    :return: Int
    '''
    if n == 1:
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(dir(factorial))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

print('-'*50)

# 변수 할당
var_func = factorial

print(var_func)
print(var_func(5))
print(list(map(var_func, range(1,6))))

# 함수 인수 전달 및 함수 결과 반환 -> 고위 함수 (Higher - oreder function)
# map, filter, reduce
print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
print([var_func(i) for i in range(1,6) if i % 2])

print('-'*50)

# reduce
from functools import reduce
from operator import add

print(reduce(add, range(1,11)))
print(sum(range(1,11)))

# 익명함수 (lambda)
# 가급적 주석 작성
# 가급적 함수 작성
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t : x + t, range(1,11)))

print('-'*50)

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(callable(str), callable(A), callable(list), callable(var_func), callable(factorial), callable(3.14))

# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(5, 10))

# 인수 고정
five = partial(mul, 5) # 5 * ?
print(five(10))
print(five(100))

# 고정 추가
six = partial(five, 6)
print(six())
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1,11))))