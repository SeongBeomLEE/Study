# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))

# 동시 선언
x = y = z = 700

# 출력
print(x, y ,z)

#선언
var = 75

# 출력
print(var)
print(type(var))

# 재 선언
var = "Change Value"

# 출력
print(var)
print(type(var))


# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔에 출력

# 예1)
print(300)

# 예2)
# n -> 777
n = 777

print(n)
print(type(n))

m = n
# m-> 777 <- n

print(m, n)
print(type(m), type(n))

m = 400
# m-> 400, 777 <-n

print(m)
print(type(m))


# id(identity)확인 : 객체의 고유값 확인
m = 800
n  = 655

print(id(m))
print(id(n))


m = 800
n  = 800

# 같은 오브젝트 참조
print(id(m))
print(id(n))

# 다양한 변수 선언
# Camel Case :  numberOfCollegeGraduates
# Pascal Case :  NumberOfCollegeGraduates
# Snake Case :  number_of_college_graduates

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""