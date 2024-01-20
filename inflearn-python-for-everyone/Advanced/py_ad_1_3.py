"""
Chapter 1
Python Advanced(1) - Shallow Copy & Deep Copy
Keyword - shallow & deep cody
"""

"""
객체의 복사 종류 : Copy, Shallow Copy, Deep Copy
정확한 이해 후 사용 -> 프로그래밍 개발 중요(문제 발생 요소)
가변: list, set, dict
"""

# Ex1 - copy
# Call by value, Call by Reffernce, Call by Share

# Call by Reffernce
a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list

print('Ex1 >', id(a_list))
print('Ex1 >', id(b_list))

b_list[2] = 100

print('Ex1 >', a_list)
print('Ex1 >', b_list)

b_list[3][2] = 100

print('Ex1 >', a_list)
print('Ex1 >', b_list)

# immutable : int, str, float, bool, unicode...

# Ex2 - shallow Copy
import copy
c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
# 안에 있는 리스트의 주소 값은 같음 따라서 값을 바꾸면 같이 바뀜
d_list = copy.copy(c_list)

print('Ex2 >', id(c_list))
print('Ex2 >', id(d_list))

d_list[1] = 100

print('Ex2 >', c_list)
print('Ex2 >', d_list)

d_list[3].append(1000)
d_list[4][1] = 10000

# 안에 있는 리스트의 주소 값은 같음
print('Ex2 >', c_list)
print('Ex2 >', d_list)

# Ex3 - deep Copy
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)

print('Ex2 >', id(e_list))
print('Ex2 >', id(f_list))

f_list[1] = 100

print('Ex2 >', e_list)
print('Ex2 >', f_list)

f_list[3].append(1000)
f_list[4][1] = 10000

# 안에 있는 리스트의 주소 값이 다름
print('Ex2 >', e_list)
print('Ex2 >', f_list)
