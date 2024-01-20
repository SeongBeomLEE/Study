# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python."
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 문자열 출력
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

# 문자열 길이
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""

escape_str1 = "Do you have a \"retro games\"?"
escape_str2 = 'What\'s on TV?'


# 출력1
print(escape_str1)
print(escape_str2)

# 탭, 줄바꿈
t_s1 = "Click \tStart!"
t_s2 = "New Line\n Check!"

# 출력2
print(t_s1)
print(t_s2)

# Raw String
# 역슬래쉬를 신경을 안씀 r로 시작
raw_s1 = r'D:\Python\python3'
raw_s2 = r"\\x\y\z\q"

# Raw String 출력
print('Raw String')
print(raw_s1)
print(raw_s2)

# 멀티라인 출력
# 역슬래쉬 사용
multi_str1 = \
"""
문자열
멀티라인 입력
테스트
"""
print(multi_str1)

multi_str2 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 문자열 연산
str_o1 = "Pythonthon"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deajeon Busan Jinju"

print(3 * str_o1)
print(str_o1 + str_o2)
# 사용할 수 있는 함수가 나옴
print(dir(str_o1))
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))  # type 확인
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
print(str(complex(12)), type(str(complex(12))))

# 문자열 함수(upper, isalnum, startswith,
# count, endswith, isalpha 등)
# 첫번째 글자 대문자
print("Capitalize: ", str_o1.capitalize())
# 끝이 s로 끝나는지 여부
print("endswith?: ", str_o2.endswith("s"))
# 리스트를 앞에 문자열로 합쳐줌
print("join str: ", str_o1.join(["I'm ", "!"]))
# 앞에 문자를 뒤에 문자로 대체
print("replace1: ", str_o1.replace('thon', ' Good'))
print("replace2: ", str_o3.replace("are", "was"))
# 앞에 문자를 기준으로 짤라서 리스트로 반환
print("split: ", str_o4.split(' '))  # Type 확인
# 정렬
print("sorted: ", sorted(str_o1))  # reverse=True
# 뒤집기
print("reversed1: ", reversed(str_o2)) #list 형 변환
print("reversed2: ", list(reversed(str_o2)))

# 반복(시퀀스) 설명
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ 확인
# __iter__이 존재하면 시퀀스 형태이다.

# 출력
for i in im_str:
    print(i)


# 슬라이싱
str_sl = 'Nice Python'

# 슬라이싱 연습
print('str_sl:', str_sl)
print('len(str_sl):', len(str_sl))
print('str_sl[0:3]:', str_sl[0:3])
print('str_sl[:len(str_sl)]:', str_sl[:len(str_sl)])
print('str_sl[:len(str_sl) - 1]:', str_sl[:len(str_sl) - 1])
print('str_sl[:]:', str_sl[:])
print('str_sl[1:4:2]:', str_sl[1:4:2])
print('str_sl[-4:-2]:', str_sl[-4:-2])
print('str_sl[1:-2]:', str_sl[1:-2])
# 뒤집기
print('str_sl[::-1]:', str_sl[::-1])
print('str_sl[::2]:', str_sl[::2])


# 아스키코드
a = 'z'

# 문자를 아스키코드 값으로 출력
print(ord(a))
# 아스키코드 값을 문자로 출력
print(chr(122))