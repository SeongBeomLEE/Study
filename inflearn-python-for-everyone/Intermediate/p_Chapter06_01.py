# 병행성(concurrency)
# 이터레이터, 제너레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args.... (iterable)
# iterable을 만드는 것이 이터레이터

# 반복 가능한 이유 -> iter() 함수 호출
t = 'ABCDEFGHIJKLMN'
print(dir(t)) # __iter__ 존재
for c in t:
    print(c)

# while (원리 파악)
w = iter(t)
print(dir(w)) # __next__ 존재
while True:
    try:
        print(next(w))
    except StopIteration:
        break
print()

# 반복형 확인
from collections import abc

print(dir(t))
print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))

print()

# next 사용 (예외처리를 해줘야 함)
class wordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iterration. ^.^')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

w1 = wordSplitter('Do today what you could do tommorrow')
print(w1)
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))
# print(next(w1))

print()

# Generater 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 증가 후 메모리 사용량 증가 -> 제너레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(corutine) 구현과 연동
# 3. 작은 메모리 조각 사용

# 내부적으로 yield 를 통해서 상태를 기억함
# yield가 코루틴이 됨
class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word # 제너레이터
        return

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wg = WordSplitGenerator('Do today what you could do tommorrow')
wt = iter(wg)

print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))



