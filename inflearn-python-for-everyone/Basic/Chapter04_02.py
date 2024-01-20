# Chapter04-2
# 파이썬 반복문
# FOR 실습

# 코딩의 핵심
# for i in <collection>
#     <loop body>

for v1 in range(10):
    print("v1 is :", v1) # 0~9 출력

print()

for v2 in range(1, 11):
    print("v2 is :", v2) # 1~10 출력

print()

for v3 in range(1, 11, 2): # 1~10 중 2 간격으로 출력
    print("v3 is :", v3)

print()

# 1 ~ 1000합

sum1 = 0
for v in range(1, 1001): # 1~1000 까지 합
    sum1 += v

print('1 ~ 1000 Sum : ', sum1)
print('1 ~ 1000 Sum : ', sum1)
print('1 ~ 1000 Sum : ', sum(range(1, 1001)))  # sum(리스트)
print('1 ~ 1000 안에 4의 배수의 합 : ', sum(range(1, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed 뒤집기, enumerate 순서를 같이 반환, filter, map, zip

# 예제1
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

for name in names:
    print("You are", name)

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
    print("Current number : ", number)

# 예제3
word = 'Beautiful'

for s in word:
    print('word : ', s)

# 예제4
my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}

for key in my_info: # key에는 딕셔너리의 key가 들어감
    print(key, ":", my_info[key]) # 각 키의 value를 반환

for val in my_info.values():
    print(val) #value 출력

# 예제5
name = 'FineApplE'

for n in name:
    if n.isupper(): # 대문자면 True
        print(n) #F, A, I, E
    else:
        print(n.upper()) # 소문자를 대문자로 변환해서 반환

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 34:
        print("Found : 34!")
        break # 34면 여기서 반복을 멈춤
    else:
        print("Not found : ", num)

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is bool:
        continue # 현재 반복을 건너 뜀

    print("current type : ", type(v)) # True를 제외하고 나머지 다 반복
    print("multiply by 2:", v * 3)

# else 구문
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 45:  # 45
        print("Found : 34!")
        break
# 반복문을 다 완료하면 else 문구를 출력
# break를 통해서 멈춘다면 else 문구를 출력하지 않음
else:
    print("Not Found 45...")


# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end='')
    print()

# 변환 예제
name = 'Aceman'
print('Reversed : ', reversed(name)) # 뒤집기
print('List : ', list(reversed(name)))
print('Tuple : ', tuple(reversed(name)))
print('Set : ', set(reversed(name)))  # 순서X