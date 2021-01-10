# 파이썬 패키지(모듈을 모아 놓은 폴더)
# 패키지와 모듈은 코드의 재사용성을 높임
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분활된 개별적인 모듈로 구성
# 상대경로 : .. (부모 디렉터리로 올라감) / .(현재 디렉토리) -> 모듈 내부에서만 사용

#__init__.py: Python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# __all__ = ['module1', 추가, 추가...]을 먼저 검색함

# 예제1

from Basic import sub
import Basic.sub.sub2.module2

Basic.sub.sub1.module1.mod1_test1()
Basic.sub.sub1.module1.mod1_test2()

Basic.sub.sub2.module2.mod2_test1()
Basic.sub.sub2.module2.mod2_test2()

print('-'*15)

# 예제2
from Basic.sub.sub1 import module1
from Basic.sub.sub2 import module2 as m2

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print('-'*15)

# 예제3
# *는 전부사용하겠다는 뜻
# 사용할 것만 정확하게 가져오는 것이 좋다
# 왜냐하면 메모리를 잡아먹기 때문이다.

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()

