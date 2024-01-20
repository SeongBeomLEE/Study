# Chapter10-2
# Hangman(행맨) 미니게임 제작(2)
# 프로그램 완성 및 최종 테스트

# 시간 처리
import time
# 랜덤
import random
# csv 처리
import csv
# 사운드 처리
import winsound
#처음 인사
name = input("What is your name? ")

print("Hi!, " + name, "Time to play hangman game!")

print()

#1초 대기
time.sleep(1)

print("Start loading...")
print()

# 0.5초 대기
time.sleep(0.5)

# CSV 단어 리스트
words = []

# 문제 CSV 파일 로드
with open('resource/word_list.csv', 'r') as f:
	reader = csv.reader(f)
	# Header Skip
	next(reader)
	for c in reader:
		words.append(c)

# 리스트 섞기
random.shuffle(words)
# 임의의 단어 선택
q = random.choice(words)

#정답 단어
word = q[0].strip()

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
		# 성공 사운드
        winsound.PlaySound('./sound/good.wav',winsound.SND_FILENAME)
		# 축하 메시지
        print("Congratulations! The Guesses is correct.")
        # while 구문 중단
        break

    print()
    # 추측 단어 글자 단위 입력
    print()
    print('Hint : {}'.format(q[1].strip()))
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
			# 탈락 사운드
            winsound.PlaySound('./sound/bad.wav',winsound.SND_FILENAME)
            # 실패 메시지
            print("You hangman game failed. Bye!")
