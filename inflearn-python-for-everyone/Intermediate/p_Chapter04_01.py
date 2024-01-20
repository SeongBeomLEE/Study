# Sequence - 시퀀스
# 시퀀스형
# 컨테이너(container : 서로 다른 자료형을 담는 것[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, collections.deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# 지능형 리스트 (comprehending lists)
chars = '+_((&^&%^^#' # 불변형
code_list1 = [ord(s) for s in chars] # 가변형으로 변환

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

# 전체 줄력
print(code_list1)
print(code_list3)
print(code_list4)

print([chr(s) for s in code_list1])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print('-'*50)

# Generator 생성
# 메모리를 효율적으로 사용할 수 있음
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(tuple_g) # generator
print(type(tuple_g))
print(next(tuple_g))

print(array_g)
print(type(array_g))
print(array_g.tolist())

# 제네레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)):
    print(s)

# 리스트 주의
# 각각의 주소값이 다름
marks1 = [['~']*3 for _ in range(4)]
# 하나의 주소값이 4개가 복사 따라서 값 1개를 수정하면 똑같은 id를 가진 모든 것이 다 수정됨
marks2 = [['~'] * 3] * 4
print(marks1)
print(marks2)

print()
# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'
print(marks1)
print(marks2)

print()
# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])
# 깊은 복사
# 얖은 복사


