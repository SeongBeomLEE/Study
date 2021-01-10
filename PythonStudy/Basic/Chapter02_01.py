# 파이썬 완전 기초
# print 사용법

# 기본 출력
print('Hellow word')
print("Hellow word")
print('''Hellow word''')
print("""Hellow word""")

print('\n')

# sep 옵션
# ,를 바꿔줌
print('H','e','l','l','o','w',' ','w','o','r','d', sep="")
print('H','e','l','l','o','w',' ','w','o','r','d', sep="_")

print('\n')

# end 옵션
print('H','e','l','l','o','w',' ','w','o','r','d', end=" ")
print('H','e','l','l','o','w',' ','w','o','r','d', end="\n")
print('H','e','l','l','o','w',' ','w','o','r','d', end="_")

# file 옵션
import sys

# 지정된 파일에 쓰겠다.
# sys.stdout는 현재 파이썬 콘솔을 의미함
print("L P", file=sys.stdout)

print('\n')

# format 사용법(d, s, f)
# d -> 정수형 / s -> 문자혈 / f -> 실수형
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{} {}'.format('one', 2))
# 인덱스에 맞춰서 값을 줌
print('{1} {0}'.format('one', 2))

print('\n')

# %s
# 총 자릿수 10자리 왼쪽 공백
print('%10s'%('12345678'))
print('{:>10}'.format("!2345678"))
# 오른쪽 공백
print('%-10s'%('12345678'))
print('{:10}'.format("!2345678"))
# 공백 부분을 _로 바꿈
print('{:_>10}'.format("!2345678"))
# 공백 부분을 $로 바꿈
print('{:$>10}'.format("!2345678"))
# 중앙정렬
print('{:$^10}'.format("!2345678"))

# .을 붙이면 5개만 출력
print('%.5s'%('12345678'))
print('%5s'%('12345678'))
# 공간은 10글자이지만 5개의 글자만 출력해라
print('{:10.5}'.format("!2345678"))

print('\n')

# %d
print('%d %d'%(1,2))
print('{} {}'.format(1,2))

print('%4d'%(122432423))
print('%4d'%(122432423))

# %f
print('%.10f'%(111.21312321322432423))
print('%01.2f'%(111.21312321322432423))
print('{:06.2f}'.format(121.1))