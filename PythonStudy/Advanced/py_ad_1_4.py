"""
Chapter 1
Python Advanced(1) - Context Manager(1) 
Keyword - Contextlib, __enter__, __exit__, exception
"""
"""
가장 대표적인 with 구문 이해
원하는 시점에 리소스 할당 및 회수
정확한 이해 후 사용 프로그래밍 개발 중요(문제 발생 요소)
"""
'''
컨텍스트 매니저: 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 변환하는 역할
가장 대표적인 with 구문 이해
정확한 이해 후 사용 프로그래밍 개발 중요 (문제 발생 요소 제거)
'''
# Ex1
file = open('./testfile1.txt', 'w')
try:
    file.write('Context Manager test1 \nContextlib Test1.')
finally:
    # 종료를 직접 적음
    file.close()

# Ex2
# 자동으로 종료
with open('./testfile1.txt', 'w') as f:
    f.write('Context Manager test2 \nContextlib Test2.')

# Ex3
# Use Class -> Context Manager with exception handling
# Context Manager
class MyFileWriter():
    def __init__(self, file_name, method):
        print('MyFileWriter started : __init__')
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print('MyfileWriter started : __enter__')
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('MygfileWriter started : __exit__')
        # 에러가 있다면
        # bool 값이 들어옴
        if exc_type:
            print(f'Logging exception {exc_type}, {exc_val}, {exc_tb}')
        self.file_obj.close()

with MyFileWriter('./testfile1.txt', 'w') as f:
    f.write('Context Manager test3 \nContextlib Test3.')
