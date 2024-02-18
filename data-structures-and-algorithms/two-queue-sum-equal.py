"""
https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/
- 두 큐 합 같게 만들기 풀이 참고
"""

from collections import deque
def solution(queue1, queue2):
    limit = len(queue1) * 3
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    cnt = 0
    if (queue1_sum + queue2_sum) % 2 != 0:
        return -1
    
    while queue1_sum != queue2_sum:
        if cnt >= limit:
            return -1
        
        while queue1 and queue1_sum > queue2_sum:
            val = queue1.popleft()
            queue2.append(val)
            queue1_sum -= val
            queue2_sum += val
            cnt += 1

        while queue2 and queue1_sum < queue2_sum:
            val = queue2.popleft()
            queue1.append(val)
            queue1_sum += val
            queue2_sum -= val
            cnt += 1
    return cnt

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1, queue2))