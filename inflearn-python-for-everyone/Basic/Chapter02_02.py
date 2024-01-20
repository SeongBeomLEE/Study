# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n*7)
print(type(n))
print()

# 동시 선언
x = y = z = 700
# 재선언
x = 100
print(x,y,z)
print()
x, y = 1, 200
print(x,y)
print()

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))
print()

# 예2)
n = 777
print(n, type(n))
print()

# m -> 777 <-n
m = n
print(m, n)
m = 100
print(m, n)
print()

# id(identity)확인: 객체의 고유값 확인
m = 800
n = 655
print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 똑같은 하나의 인스턴스로 파이썬 내부에서 동작함
# 생산성과 효율성을 위해서 이렇게 해석함
m = 800
n = 800
print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언 방법
# Camel Case : numberOfCollegeGra -> Method
# Pascal Case : NumberOfCollegeGra -> Class
# snake Case : number_of_college_gra -> 변수 선언

# 허용하는 변수 선언 법
age = 1
ageOfAge = 1
age_of_age = 1

# 변수의 시작은 특수문자. 숫자 불가능 그러나 _는 가능
# 예약어는 변수명으로 불가능
