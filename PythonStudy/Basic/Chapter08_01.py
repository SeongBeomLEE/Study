# 파이썬 내장 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습

# 절대값
# abs()
print(abs(-3))

# all, any : iterable 요소 검사 (참, 거짓)
print(all([1,2,3])) # and / 안에 요소들이 모두 True
print(all([1,2,0])) # and / 0 존재 False

print(any([1,2,3])) # or / 안에 요소들이 모두 True
print(any([1,2,0])) # or / 0 존재 False 지만 or 조건

# chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(67))
print(ord('C'))

# enumerate : 인덱스 + interable 객체 생성
for idx, value in enumerate(['aa','bb']):
    print(idx,value)

# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv(x):
    return abs(x) > 2

print(list(filter(conv, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x : abs(x) > 2, [1, -3, 2, 0, -5, 6])))

# id : 객체의 주소값(레퍼런스)
print(id(5))

# len : 요소의 길이 반환
print(len('aasasasas') - 1)
print(len([12,12,231,123,213]))

# max, mix : 최대값, 최소값
print(max([1,2,3]))
print(max('pythonstudy'))
print(min([1,2,3]))
print(min('pythonstudy'))

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1,-3,2,0,-1,-4,-5])))
print(list(map(lambda x : abs(x), [1,-3,2,0,-1,-4,-5])))

# pow : 제곱값 반환
print(pow(2,4))

# range : 반복가능한 객체(Iterable) 반환
print(list(range(0,10,2)))

# round : 반올림
print(round(6.5781, 2))
print(round(6.5781))

# sorted : 반복가능한 객체를 정렬 후 반환
print(sorted([8,5,7,2,3,9,3,3]))
print(sorted(['p','y','t','h','o','n']))

# sum : 반복가능한 객체를 더한 후 반환
print(sum([8,5,7,2,3,9,3,3]))

# type : 자료형 확인
print(type([12112]))

# zip : 반복가능한 객체의 요소를 묶어서 반환 (짝이 맞아야 함)
for i,v in zip([1,2,3],[4,5,6]):
    print(i,v)

print(list(zip([1,2,3],[4,5,6]))) # 리스트 내부 원소의 형태는 튜플