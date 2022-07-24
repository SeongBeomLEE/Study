# Machine-Learning-Engineer-Interview

Machine Learning Engineer가 되기 위한 기본 지식을 정리하고 있습니다!

노션에서 보고 싶으시면 해당 [링크](https://abyssinian-decade-924.notion.site/712eda7179d34e9393c49ff8fbd1d873?v=705a41dac2b84b4c8fedf0141ca2e3c6)를 클릭해주세요!(노션은 복습의 용도로 정리하고 있어서 업데이트가 느릴 수 있습니다!)

제가 정리한 내용 중에 질문 or 피드백이 있으시다면 언제든지 PR과 issue를 남겨주세요!

## [확률과 통계](https://github.com/SeongBeomLEE/Machine-Learning-Engineer-Interview/blob/main/Probability-and-Statistics.md)
- 통계학이란

- 평균과 중앙값

- 심슨의 역설

- 상관 관계와 인과 관계

- 선험적 확률과 경험적 확률

- 기댓값, 분산, 공분산, 상관계수, 공분산 행렬

- 확률변수, 확률 분포, 확률 밀도 함수, 누적 분포 함수, 확률 질량 함수, 누적 질량 함수

- 이항 분포

- 기하 분포

- 포아송 분포

- 지수 분포

- 중심극한정리

- 카이 제곱 분포

- 모집단, 모수, 표본, 표준 오차

- 검정 통계량

- t-value (두 개의 표본을 비교할 때 사용 - 평균을 활용)

- F-value (여러 개의 표본을 비교할 때 사용 - 분산을 활용)

- 귀무가설과 대립가설

- p-value

- 신뢰 구간

- 1종 오류와 2종 오류

- 모수적 모델, 비모수적 모델

- 빈도주의 통계와 베이지안 통계

- 베이즈 정리

- Maximum Likelihood Estimation와 Maximum A Posterior

- Entorpy와 정보 이론

- Cross Entropy

- KL-Divergence

- 감마 분포
    - https://m.blog.naver.com/mykepzzang/220842759639

- 베타 분포
    - https://m.blog.naver.com/mykepzzang/220843077734

- Boxplot

- A/B Test

## [선형대수학](https://github.com/SeongBeomLEE/Machine-Learning-Engineer-Interview/blob/main/Linear-Algebra.md)
- 선형대수학이란

- 선형성과 비선형성

- 벡터, 벡터의 기본 연산

- 선형독립과 선형종속 그리고 다중공선성

- L1 norm과 L2 norm + L1 Regularization과 L2 Regularization

- 벡터의 내적

- 코사인 유사도와 내적 유사도

- 행렬곱

- 행벡터의 의미와 벡터의 내적

- 선형변환

- 행렬식의 기하학적 의미

- 고윳값과 고유벡터

- PCA

- EVD

- SVD

- 선형대수와 푸리에 변환

- 순환행렬과 컨볼류션

- 순환행렬의 고유벡터, 그리고 푸리에 행렬

- 상관계수는 벡터의 내적이다
- 기저 벡터

## Machine Learning
- Confusion Matrix

- 편향과 분산

- ROC-curve

- Linear Regression

- Logistic Regression

- SVM

- Decision Tree

- 배깅

- 부스팅

- RandomForest

- AdaBoost

- 앙상블

## Deep Learning
- 경사하강법

- local minimum과 global minimum

- Optimazor

- Batch Norm

- MLP

- CNN

- RNN

- LSTM

- GRU

- Transformer

- AutoEncoder

- VAE
    - https://hyeongminlee.github.io/post/bnn003_vi/

- GAN

- BERT

- GPT

- Representation Learning

- 모델의 overfitting이 일어났을 때 해결하는 방법

- 데이터 불균형에 대응 하는 방법

## NLP
- TF-IDF

- Word2Vec

- 언어 모델

- N-gram 언어 모델

## RecSys
- Multi-Armed Bandit

- Cold-start-Problem
    - content-based Model, 초기 유저 정보 수집

## Python
- global interpreter lock

- Flask의 장점과 단점

- Flask에서 WSGI가 무엇인지

- 깊은 복사와 얕은 복사 (list와 엮어서)

- global과 nonlocal

- 파이썬 Mutable과 Immutable의 차이

- 파이썬 Map에서 Value로 정렬하는 방법

- 파이썬 List Comprehension

- 파이썬 list와 tuple의 차이

- 파이썬 set 구현 방식

- 파이썬 list 구현 방식, insert / get 시간 복잡도

- 파이썬 dictionary 구현 방식, insert / get 시간 복잡도

- 파이썬 dequeue 구현 방식, insert / get 시간 복잡도

- 파이썬에서 key가 될 수 있는 것은? list는 키가 될 수 있을까? (key에 list나 tuple을 쓸 수 있는가)

- 파이썬에서의 해쉬 맵 내부구조를 설명하세요.

- 파이썬에서의 멀티 스레드의 단점

- Linked List에서 순환 구조를 찾는 방법

- Binary Search 사용시 최악의 경우의 예와 대처 방법

- Stable sorting이란?

- 클래스는 무엇이며, 클래스의 장점은 무엇인가요?

## CS

- 배열

- 연결리스트

- 스택

- 큐

- 덱(deque)

- 자바에서의 상속에 대해서 설명

- 자바에서의 추상클래스는 인스턴스 생성이 가능한가?

- 자바에서의 오버라이딩과 오버로딩의 차이

## MLOps
- ML-System-design-pattern

- Docker

- Airflow

- GCP

- 쿠버네티스