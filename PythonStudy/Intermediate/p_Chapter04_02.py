# Sequence - 시퀀스
# 시퀀스형
# 컨테이너(container : 서로 다른 자료형을 담는 것[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, collections.deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# 튜플 어드밴드
# 언팩킹

# b, a = a, b

print(divmod(100,9))
# * 언팩킹해서 값을 넣어라
print(divmod(*(100,9)))
print(*(divmod(100,9)))

print('-'*30)

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print('-'*30)

# Multable (가변) VS Immutable(불변)
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

print(l, id(l))
print(m, id(m))

# 튜플은 계속 바뀜, 리스트는 연산자의 활용에 따라 다름

print('-'*30)

# sort vs sorted
# reverse, key=len, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환 (원본 수정 X)
# sort : 정렬 후 객체 직접 변경 (원본 수정 O)
f_list = ['oo', 'aaa', 'mmmmm', 'ppppp', 'lll', 'ssss', 'ccc']
print('sorted - ',sorted(f_list))
print('sorted - ',sorted(f_list, reverse=True))
print('sorted - ',sorted(f_list, key=len))
print('sorted - ',sorted(f_list, key=lambda x : x[-1]))
print('sorted - ',sorted(f_list, key=lambda x : x[-1], reverse=True))

print('sorted - ', f_list)

# sort : 정렬 후 객체 직접 변경 (원본 수정 O)

# 반환 값 확인(None)
print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse=True), f_list)
print('sort - ', f_list.sort(key=len), f_list)
print('sort - ', f_list.sort(key=lambda x : x[-1]), f_list)
print('sort - ', f_list.sort(key=lambda x : x[-1], reverse=True), f_list)

print(f_list)

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융퉁성, 다양한 자료형, 범용적 사용 (다양한 형식의 데이터)
# 숫자 기반 : 배열(리스트와 거의 호환)