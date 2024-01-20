# 병행성(concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램에서 여러 일을 쉽게 해결 (파이썬의 큰 장점)
# 병렬성(parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# Generator ex1
def generator_ex1():
    print('Strat')
    yield 'A point' # 네이버에서 크롤링
    print('Continue')
    yield 'B point' # 구글에서 크롤링 (위치를 기억하고 있기 때문에 가능)
    print('End')

temp = iter(generator_ex1())

# print(temp)
# print(next(temp)) # 위치를 기억하고 있음 (따라서 병행성이 가능함)
# print(next(temp))
# print(next(temp))

# for v in generator_ex1():
#     print(v)

# Generator ex2
temp2 = [x * 3 for x in generator_ex1()] # x에 들어가는 것은 yield에 지정한 값
temp3 = (x * 3 for x in generator_ex1())

print(temp2)
print(temp3)

for i in temp2:
    print(i)

for i in temp3:
    print(i)

print()

# Generator ex3(중요 함수)
# count, takewhile, filterfalse, accumulate, chain, product, groupby...

import itertools

gen1 = itertools.count(1, 2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# .... 무한

# 조건
# gen2 = itertools.takewhile(lambda n : n < 10, itertools.count(1, 2.5))
# for v in gen2:
#     print(v)

print()

# 필터반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])
for v in gen3:
    print(v)

print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1,10)])

for v in gen4:
    print(v)

# 연결1
gen5 = itertools.chain('ABCDE', range(1,11,2))
print(list(gen5))

# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

# 개별
gen7 = itertools.product('ABCDE')
print(list(gen7))

# 연산(경우의수)
# repeat만큼의 순서쌍을 반환해줌
gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8))

# 그룹화
gen9 = itertools.groupby("AAABBBCCCCDDDEEEE")
# print(list(gen9))

for chr, group in gen9:
    print(chr, ':' ,list(group))
