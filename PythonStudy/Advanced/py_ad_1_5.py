"""
Chapter 1
Python Advanced(1) - Context Manager(2) 
Keyword - Contextlib, __enter__, __exit__
"""
"""
Contextlib - Measure execution(타이머) 제작
"""

# Ex1
# Use Class
import time

class ExcuteTimer(object):
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'Logging exception {exc_type}, {exc_val}, {exc_tb}')
        else:
            print(f'{self._msg} : {time.monotonic() - self._start} s ')
        return True

with ExcuteTimer('Start! job') as v:
    print(f'Recived start monotonic1 : {v}')
    # Excute job
    for i in range(100000):
        pass
    raise Exception('Raise Exception!!') # 강제로 에러 발생