# Chapter06-03
# 흐름제어, 병행성(Concurrency)
# 코루틴(Coroutine)

# yield : 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송
# yield from

# 서브루틴 : 메인루틴에서 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 ->  동시성 프로그래밍
# 코루틴 : 쓰레드에 비해 오버헤드 감소
# 쓰레드 : 싱글쓰레드 -> 멀티쓰레드 -> 복잡 -> 공유되는 자원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가

# 코루틴 Ex1
def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 제네레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))

# yield 지점 까지 서브루틴 수행
# next(cr1)

# 기본 전달 값 None
# next(cr1)

# 값 전송
# cr1.send(100)

# 잘못된 사용

cr2 = coroutine1()

# cr2.send(100) # 예외 발생

# 코루틴 Ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))


cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))

print(next(cr3))

print(getgeneratorstate(cr3))

print(cr3.send(15))

# print(c3.send(20)) # 예외

print()
print()

# 코루틴 Ex3
# StopIteration 자동 처리(3.5 -> await)
# 중첩 코루틴 처리
def generator1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y

t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))

t2 = generator1()

print(list(t2))

print()
print()

def generator2():
    yield from 'AB'
    yield from range(1,4)


t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
# print(next(t3))

print()
print()