# Chapter04-1
# 파이썬 제어문
# IF 실습

# 기본 형식
print(type(True)) # 0이 아닌 수, 'abc', [1,2,3,4],(1,2,3)...
print(type(False)) # 0, "", [], {}, ()...

# 예1
if True:
    print("Good")  # 들여쓰기(Indent)

if False: print("Bad") # 실행 X

# 예2
if False: print("Bad") # 여기는 실행되지 않음.
else: print("Good") # 여기가 실행된다.

# 관계연산자 종류
# >, >=, <, <=, ==, !=

x = 15
y = 10

# == 양 변이 같을 때 참.
print(x == y) # False

# != 양 변이 다를 때 참.
print(x != y) # True

# > 왼쪽이 클때 참.
print(x > y) # True

# >= 왼쪽이 크거나 같을 때 참.
print(x >= y) # True

# < 오른쪽이 클 때 참.
print(x < y) # False

# <= 오른쪽이 크거나 같을 때 참.
print(x <= y) # False

# 참 거짓 판별 종류
# 참 : "values", [values], (values), {values}, 1
# 거짓 : "", [], (), {}, 0, None

city = "" # False로 해석
if city: print("You are in:", city)
else: print("Please enter your city") #출력

city = "Seoul" # True로 해석
if city: print("You are in:", city) #출력
else: print("Please enter your city")

# 논리연산자(중요)
# and, or, not
# 참고 : https://www.tutorialspoint.com/python/python_basic_operators.htm

a = 75
b = 40
c = 10

print('and : ', a > b and b > c)  # a > b > c # True
print('or : ', a > b or b > c) # True
print('not : ', not a > b) # False
print('not : ', not b > c) # False
print(not True) # False
print(not False) # True

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리 순서로 적용

print('e1 : ', 3 + 12 > 7 + 3) # True
print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)  # False
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10) # True
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10) # False

score1 = 90
score2 = 'A'
# 복수의 조건이 모두 참일 경우에 실행.
if score1 >= 90 and score2 == 'A':
    print("Pass.") # 실행
else:
    print("Fail.")

# 예제
id1 = "vip"
id2 = "admin"
grade = 'platinum'

if id1 == "vip" or id2 == "admin": #True
    print("관리자 인증") # 실행

if id2 == "admin" and grade != "platinum": #False
    print("최상위 관리자") # 실행안함


# 다중 조건문
num = 90

# 위에 조건이 만족하면 종료
if num >= 90:
    print('Grade : A') #출력
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')

# 중첩 조건문

grade = 'A'
total = 95

if grade == 'A':
    if total >= 90: print("장학금 100%") #출력
    elif total >= 80: print("장학금 80%")
    else: print("장학금 70%")
else: print("장학금 50%")

# in, not in

q = [10, 20, 30]
w = {70, 80, 90, 90}
e = {"name": 'Lee', "city": "Seoul", "grade": "A"}
r = (10, 12, 14)

print(15 in q) # False
print(90 in w) # True
print(12 not in r)  # False
print("name" in e)  # key 검색  # True
print("Seoul" in e.values())  # value 검색  # True