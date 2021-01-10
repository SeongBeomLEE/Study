# 병행성(concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램에서 여러 일을 쉽게 해결 (파이썬의 큰 장점)
# 병렬성(parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도
# 코루틴(coroutine)

# 코루틴 : 단일(싱글) 스레드, 스택을 기반으로 동작하는 비동기 작업
# 스레드 : OS에서 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티쓰레드
# yield, send : 메인 <-> 서브 (양방향 소통 가능)
# yield는 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인 루틴에서 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴 : 스레드에 비해 오버헤드 감소
# 스레드 : 싱글스레드 -> 멀티스레드 -> 복잡 -> 공유되는 지원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가
# def -> async, yield -> await

# 코루틴 ex1
# 서브루틴
def coroutine1():
    print(">>> coroutine started.")
    i = yield
    print(">>> coroutine received : {}".format(i))

# 메인 루틴
# 제너레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))

# # yield 지점까지 서브루틴 수행
# next(cr1)
# # 기본 전달 값 None
# next(cr1)
# # 값 전송
# cr1.send(100)

# 잘못된 사용
cr2 = coroutine1()
# cr2.send(100)

# 코루틴 ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print(">>> coroutine started : {}".format(x))
    y = yield x
    print(">>> coroutine received : {}".format(y))
    z = yield x + y
    print(">>> coroutine received : {}".format(z))

cr3 = coroutine2(10)

from inspect import getgeneratorstate

# print(getgeneratorstate(cr3))
# print(next(cr3)) # 값은 10을 받았고 y를 받을 상태
# print(getgeneratorstate(cr3))
# print(cr3.send(100))
# print(getgeneratorstate(cr3))
# print(cr3.send(200))
# print(getgeneratorstate(cr3))

print()

# 코루틴 ex3
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

def generator2():
    yield from "AB"
    yield from range(1,4)

t3 = generator2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
# print(next(t3))

print()

print(list(t3))
