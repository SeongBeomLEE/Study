# Chapter06-2
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y

# import 한 코드에서 나오는 문구
print('-' * 15)
print('called! inner!')
print(add(5,5))
print(subtract(15,5))
print(multiply(5,5))
print(divide(10,2))
print(power(5,3))
print('-' * 15)
print(__name__)

# __name__ 사용
# 현재 코드에서 사용하면 나오는 화면
if __name__ == "__main__":
    print('-' * 15)
    print('called! __main__')
    print(add(5, 5))
    print(subtract(15, 5))
    print(multiply(5, 5))
    print(divide(10, 2))
    print(power(5, 3))
    print('-' * 15)
    print(__name__)