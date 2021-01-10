# 파이썬 심화
# 클로저 기초

# 파이썬 변수 범위(scope)

# ex1
def FuncV1(a):
    print(a)
    print(b)

# FuncV1(10)

# ex2
b = 20

def FuncV2(a):
    print(a)
    print(b)

FuncV2(10)

# ex3
c = 30

def FuncV3(a):
    global c
    print(a)
    print(c)
    c = 40

print('>>>', c)
FuncV3(10)
print('>>>', c)

# CLosure(클로저) 사용 이유 (클로저는 상태를 기억한다)
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착 상태 (Dead Lack)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 -> Erlang
# 클로저는 공유하되 변경되지 않는 (Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(coroutine) 프로그래밍에 강점

a = 100
print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1,51)))
print(sum(range(51,101)))

# 클래스 이용
class Averager():
    def __init__(self):
        self._serices = []

    # 클래스를 함수 형태처럼 사용할 수 있게 만들어 줌
    def __call__(self, v):
        self._serices.append(v)
        print('inner >>> {} / {}'.format(self._serices, len(self._serices)))
        return sum(self._serices) / len(self._serices)

# 인스턴스 생성
average_cls = Averager()
print(dir(average_cls))

# 누적
print(average_cls(10))
print(average_cls(30))
print(average_cls(50))
print(average_cls(70))
print(average_cls(193))
