# Chapter10-1
# Hangman(행맨) 미니게임 제작(1)
# 기본 프로그램 제작 및 테스트

# 시간 처리
import time

#처음 인사
name = input("What is your name? ")

print("Hi!, " + name, "Time to play hangman game!")

print()

#1초 대기
time.sleep(1)

print("Start loading...")
print()
time.sleep(0.5)

#정답 단어
word = "secret"

#추측 단어
guesses = ''

#기회
turns = 10

# 핵심 While Loop
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    # 실패 횟수
    failed = 0

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 단어가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print (char, end=' ')
        else:
            # 틀린 경우 대시로 처리
            print ("_", end=' ')
            # 실패 횟수 증가
            failed += 1

    # 단어 추측이 성공한 경우
    if failed == 0:
        print()
        print()
        print("Congratulations! The Guesses is correct.")
        # while 구문 중단
        break

    print()

    # 추측 단어 글자 단위 입력
    print()
    guess = input("guess a character:")

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        # 기회 횟수 감소
        turns -= 1
        # 오류 메시지
        print("Oops! Wrong")
        # 남은 기회 출력
        print("You have", + turns, 'more guesses!')

        # 기회를 모두 사용하면
        if turns == 0:
            # 실패 메시지
            print("You hangman game failed. Bye!")
