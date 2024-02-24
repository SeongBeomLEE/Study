"""
- 목표
-- 다음 달에 선물을 주고 받을 때, 가장 많은 선물을 받는 친구의 선물의 수를 얻고 싶음

- 경우 1 (두 사람이 선물을 주고받은 기록이 있을 때)
-- A가 B에게 선물을 준 횟수 > B가 A에게 선물을 준 횟수
-- 다음 달에 A는 B에게 선물을 1개 받음

- 경우 2 (두 사람이 선물을 주고받은 기록이 없거나, 주고 받은 수가 같은 경우)
-- 선물 지수 = 준 선물 - 받은 선물
-- 선물 지수가 큰 친구에게 선물을 1개 줌
-- 선물 지수가 같으면 서로 선물을 주고 받지 않음

- 필요 기능
-- 각 친구들에게 선물을 준 횟수를 구해야 함
-- 선물 지수를 구해야 함
"""

def solution(friends, gifts):
    friend_to_index = {friend:index for index, friend in enumerate(friends)}
    friend_index_to_swap_gift_count_list = [[0]*len(friends) for _ in range(len(friends))]
    friend_to_gift_count = {friend:0 for friend in friends}
    friend_to_swap_gift_friends = {friend:set() for friend in friends}
    
    for gift in gifts:
        A, B = gift.split()
        A_index, B_index = friend_to_index[A], friend_to_index[B]
        
        # 각 친구들에게 선물을 준 횟수 저장
        friend_index_to_swap_gift_count_list[A_index][B_index] += 1
        
        # 선물을 주고 받은 경우 저장
        friend_to_swap_gift_friends[A].add(B)
        friend_to_swap_gift_friends[B].add(A)
        
        # 선물 지수 계산
        friend_to_gift_count[A] += 1
        friend_to_gift_count[B] -= 1
    
    answer = 0
    for A in friends:
        now = 0
        A_index = friend_to_index[A]
        for B in friends:
            B_index = friend_to_index[B]

            # 두 사람이 선물을 주고받은 기록이 있을 때
            if B in friend_to_swap_gift_friends[A]:
                if friend_index_to_swap_gift_count_list[A_index][B_index] > friend_index_to_swap_gift_count_list[B_index][A_index]:
                    now += 1
                    continue
            
            # 두 사람이 선물을 주고받은 기록이 없거나, 주고 받은 수가 같은 경우
            if friend_index_to_swap_gift_count_list[A_index][B_index] == friend_index_to_swap_gift_count_list[B_index][A_index] or B not in friend_to_swap_gift_friends[A]:
                if friend_to_gift_count[A] > friend_to_gift_count[B]:
                    now += 1
        
        answer = max(now, answer)
    return answer

friends, gifts = ["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

print(solution(friends, gifts))