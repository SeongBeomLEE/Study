# 파이썬 딕셔너리 (사전형)
# json과 매우 유사
# 범용적으로 가장 많이 사용
# 딕셔너리 저료형(순서X, 키 중복X, 수정O, 삭제O)

# 선언
# key와 value로 이루어져 있다.
# key는 숫자로도 지정 가능
# a = {1 : ["kim", 'lee', 'lee']}
a = {'name' : ["kim", 'lee', 'lee'],
     'city' : ['s', 'b', 'c'],
     'grade': 90}

d = dict([
    ('name' , ["kim", 'lee', 'lee']),
    ('city' , ['s', 'b', 'c']),
    ('grade', 90)
])

f = dict(
     name = ["kim", 'lee', 'lee'],
     city = ['s', 'b', 'c'],
     grade = 90
)

print('a -', type(a), a)
print('d -', type(d), d)
print('f -', type(f), f)

# 출력
print('a[\'name\']:', a['name']) # key가 존재하지 않으면 에러 발생
print('a.get(\'name\'):', a.get('name')) # key가 존재하지 않으면 None

# 딕셔너리 추가
a['address'] = 'seoul'
print(a)

# key의 길이 확인
print('a -', len(a))
print('d -', len(d))
print('f -', len(f))

# dict_keys, dict_values, dict_items : 반복문에서 사용
print(a.keys())
print(a.values())
print(a.items())

# 리스트 변환
print(list(a.keys()))
print(list(a.values()))

print(a.pop('name'))
print(a)

print(a.popitem())
print(a)

# 키를 포함하고 있는지 여부
print('name' in a)

# 수정 & 추가
a['test'] = 'td'
print(a)
a['address'] = 'df'
print(a)
a.update(name = '1212')
print(a)
d['name'] = d['name'] + ["key"]
print(d)