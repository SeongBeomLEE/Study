# 추천 시스템

## 추천 시스템 이란?
- 우리는 이제 정보의 풍요를 넘어선 정보의 홍수 속에서 살게됨
- 정보의 홍수 속에서 우리는 원하는 걸 어떤 키워드로 찾아야 하는 지 모를 수 있고, 많은 정보 중에서 나에게 맞는 정보를 찾는데 많은 시간이 걸림
- 이러한 정보의 홍수 속에서 나에게 가장 필요한 정보를 빠르게 찾거나 제공받는 기술이 바로 추천 시스템이라고 할 수 있음

## 추천 시스템에서 사용되는 대이터
- 크게 유저 관련 Data, 아이템 관련 Data, 유저-아이템 상호작용 Data로 나뉘어짐
- 유저 관련 Data는 유저의 정보를 수집하는 유저 프로파일링을 통해서 얻은 정보를 의미함(유저 ID, 디바이스 ID 등의 식별자 정보 등)
- 아이템 관련 Data는 아이템의 정보를 수집하는 아이템 프로파일링을 통해서 얻은 정보를 의미함(다양한 아이템의 특성 정보 등)
- 유저-아이템 상호작용 Data는 로그에 아이템에 대한 유저의 직접적인 선호 정보가 담겨져 있는 Explicit Feedback Data와 로그에 아이템에 대한 유저의 직접적인 선호 정보가 담겨져 있지 않은 Implicit Feedback Data로 나뉘어짐

## Offline Test와 Online A/B Test
- Offline Test는 유저로 부터 수집한 데이터를 Train / Val / Test 로 나누어 모델의 성능을 객관적인 지표로 평가하는 것
- Offline Test에서 중요하게 생각해야 할 부분은 Offline Test의 좋은 성능이 Online 에서의 좋은 성능을 보장하지 않는다는 것
- Offline Test에서 사용된 데이터는 축척되지 않는 과거의 데이터지만, 실제 Online 환경에서는 실시간으로 축척되는 데이터이고 유저의 관심은 실시간으로 바뀔 수 있기 때문에, 모델의 결과가 실제 서비스와 다른 양상을 보여주는 Serving bias가 나타날 수 있음
- Online A/B Test는 Offline Test에서 검증된 가설이나 모델을 실제 서비스에서 실험해보는 단계를 의미
- 대조군(A, 새로운 추천시스템 미적용), 실험군(B, 새로운 추천시스템 적용) 간의 성능을 평가함(A와 B 환경은 최대한 동일해야 함)
- 최종 의사결정에 반영되는 마지막 Test이기 때문에 매출, CTR, PV(Page View) 등의 비즈니스/서비스 지표를 사용해 모델의 성능을 평가

## Association Rule Analysis
- Association Rule Analysis은 주어진 transaction(거래 내역, 장바구니 등) 데이터에 대해서, 하나의 itemset이 등장했을 때 다른 itemset이 같이 등장하는 규칙을 찾는 분석임
- 흔히 장바구니 분석 혹은 서열 분석이라고도 불리며, 상품의 구매, 조회 등 하나의 연속된 거래들 사이의 규칙을 발견하기 위해 사용됨
- 연관 규칙 분석은 우선 정의한 척도(support, confidence, lift)의 최솟값을 만족하는 모든 itemset을 생성하는 작업(Frequent Itemset Generation)을 거친 뒤에, 해당 itemset을 바탕으로 association rule을 생성하여 규칙을 분석함
- Brute-force Approach은 말 그대로 개별 트랜잭션의 아이템들을 풀스캔하여 가능한 모든 itemset의 support를 계산하는 방법
- Apriori 알고리즘은 가능한 후보 itemset의 개수(M)를 줄이는 방법
- DHP 알고리즘은 탐색하는 transaction의 숫자(N)를 줄이는 방법
- FP-Growth 알고리즘은 탐색횟수(NM)를 줄이는 방법

## Content-based
- 컨텐츠 기반 추천은 유저가 선호하는 아이템을 기반으로 해당 아이템과 유사한 아이템을 추천해주는 방식
- 아이템의 특징을 바탕으로 추천을 하기 때문에 유저에게 추천을 할 때 다른 유저의 데이터가 필요하지 않음
- 새로운 아이템에 대한 특징 벡터만 얻을 수 있다면 현재 존재하는 아이템들 간의 유사도를 구할 수 있기 때문에 새로운 아이템 혹은 인기도가 낮은 아이템을 추천할 수 있음
- 아이템의 특징에 기반한 추천을 하기 때문에 추천 아이템에 대한 설명(explanation)이 가능함
- 그러나 이템의 적합한 피쳐를 찾는 것이 어렵기 때문에 상당한 도메인 지식이 필요함
- 비슷한 분야와 장르의 아이템은 특징 또한 서로 비슷하기 때문에 분야/장르의 추천 결과만 계속 나올 수 있음
- 아이템에 특징을 바탕으로 추천을 사용하기 때문에 다른 유저의 데이터를 활용할 수 없어 개인화된 추천이 어려울 수 있음

## Collaborative Filtering
- 협업 필터링은 많은 유저들로부터 얻은 기호 정보를 이용해 유저의 관심사를 예측하는 방법
- 더 많은 유저/아이템 데이터가 축척될수록 협업의 효과는 커지고 추천을 정확해질 것이라는 가정에서 출발함
- Collaborative Filtering은 Content-based와 달리 아이템에 대한 특징을 따로 추출하지 않아도 되기 때문에 도메인 지식으로 부터 자유롭다는 장점을 가짐
- 유저에 대한 피트백 정보가 적다면 성능이 저하된다는 단점이 존재함
- 또한 아이템이나 유저가 계속 늘어날 경우 때 그때 마다 다시 계산해야 하기 때문에 확장성이 떨어진다는 단점이 존재함
- 이에 두 가지 방법을 모두 활용하는 Hybrid 방법도 존재하고, 다양한 모델을 앙상블하기도 함

## 유사도 측정법
- Mean Squared Difference Similarity, Cosine Similarity, Pearson Similarity, Jaccard Similarity

## Latent Factor Model
- Latent Factor Model은 유저와 아이템 관계를 잠재적 요인으로 표현할 수 있다고 보는 모델
- 다양하고 복잡한 유저와 아이템의 특성을 몇 개의 벡터로 compact하게 표현함
- Latent Factor Model은 유저-아이템 행렬을 저차원의 행렬로 분해하는 방식으로 작동함
- 학습된 Latent Factor Model의 벡터 공간에 유저와 아이템 벡터가 같은 공간에 놓일 경우 유저와 아이템의 유사한 정도를 확인할 수 있음
- 그러나 각 차원의 의미는 모델 학습을 통해 생성되며 표면적으로는 알 수 없다는 단점이 존재함
- 그럼에도 각 차원에는 데이터의 패턴이 내재되어 있기 때문에 데이터만 많다면 좋은 성능을 보임

## Matrix Factorization
- Matrix Factorization는 유저와 아이템의 상호작용을 내적으로 표현하여 implicit 또는 explicit feedback을 계산하고 이 값을 바탕으로 모델이 업데이트가 되는 방식
- 여기서 내적이 큰 값을 가지게 하기 위해서는 두 벡터가 서로 같은 방향을 바라보고 크기가 커야 하며, 이에 두 벡터의 각 차원은 서로 동일한 의미를 가짐
- 따라서 latent space의 각 차원은 유저와 아이템의 상호작용을 표현할 수 있는 무언가라고 할 수 있음
- 아이템과 유저를 표현하는 두 벡터의 방향이 최대한 비슷하고 크기가 클 수록 유저가 해당 아이템을 선호할 확률이 높음

## Bayesian Personalized Ranking
- Bayesian Personalized Ranking은 관측된 데이터를 positive로, 비관측된 데이터를 negative로 설정하고, 해당 item 쌍을 활용하고 관측된 아이템이 비관측된 아이템 보다 선호한다는 가정으로 모델을 학습시키는 방법
- 모델을 학습시킬 때 아이템 쌍은 무조건 관측된 아이템과 비관측된 아이템으로만 구성하여 단순히 관측 아이템과 비관측 아이템 사이에 선호도의 우열, 즉 순위를 매기는 것에 모델이 집중하게 만듬
- 관측된 아이템은 관측되지 않은 다른 아이템보다 선호한다는 느낌으로 아이템의 순서를 매기는 것에 집중하여 개인화된 추천에 걸맞는 최적화 방법
- 본 loss는 pos와 neg는 서로 최대한 멀어지게 학습하면서, 비슷한 latent space를 가지는 item 끼리는 가깝게 하여 아이템의 순위를 매기는데 최적화된 Loss라고 할 수 있음

## Item2Vec
- Embedding은 주어진 데이터를 낮은 차원의 벡터(vector)로 만들어서 표현하는 방법임
- 데이터를 Dense Representation 표현함으로써 공간의 낭비가 발생하지 않음
- 그러나 차원 자체가 하이퍼 파라미터라고 할 수 있음
- Item2Vec은 SGNS에서 영감을 받아 아이템 기반 CF(IBCF)에 Word2Vec을 적용한 방법임
- 즉 아이템을 Embedding으로 표현하는 방법이라고 할 수 있음
- 유저가 소비한 아이템 리스트를 문장으로, 아이템을 단어로 가정하여 Word2Vec 사용함
- Item2Vec은 유저-아이템 관계를 사용하지 않기 때문에 유저 식별 없이 세션 단위로도 데이터를 생성할 수 있음
- 시퀀스를 집합으로 바꾸면서 공간적/시간적 정보는 사라짐, 그러나 시퀀스를 시간 단위로 스플릿 한다면 시간적 정보도 반영할 수도 있을 것임

## Approximate Nearest Neighbor
- Approximate Nearest Neighbor는 효과적이고 효율적인 서빙을 위해서 정확도를 조금 포기하더라도 아주 빠른 속도로 주어진 Vector의 근접 이웃을 찾는 알고리즘임
- 즉, Approximate Nearest Neighbor는 Vector Space Model에서 내가 원하는 Query Vector와 가장 유사한 Vector를 찾는 알고리즘임

## Neural Collaborative Filtering
-  MF의 interaction function으로 사용되는 내적의 경우에는 같은 가중치로 선형 결합이 일어나고, 각 차원의 latent vector 들은 서로 독립적이라는 특징을 가짐
- 이에 단순하고 고정적인 inner product의 방식은 유저와 아이템의 복잡한 상호작용을 제대로 캡쳐하지 못해, 위 그림처럼 a large ranking loss를 발생시켜서 이를 해결하고자 interaction function으로 딥러닝을 사용하는 Neural Collaborative Filtering 방법이 생김
- Neural Collaborative Filtering는 interaction function을 어떻게 구성하느냐에 따라서 GMF, MLP, GMF와 MLP를 퓨전한 NueMF로 나뉘어짐
- GMF는 단순히 내적의 차원을 1차원으로 바꿔주는 하나의 선형 레이어를 지나서 활성화 함수를 거치는 구조임
- MLP는 interaction function을 단순히 MLP로 구성한 구조임
- NueMF는 GMF와 MLP의 퓨전한 모델로, GMF는 유저와 아이템의 상호 작용을 선형으로 표현하고, MLP는 비선형으로 표현하여, 이 두 모델의 장점을 모두 가지는 모델임

## GNN-based
- Graph 자료 구조는 관계, 상호작용과 같은 추상적인 개념을 다루기에 적합함
- GNN은 Graph 자료 구조를 표현할 수 있는 신경망임
- GCN은 local connectivity, shared weights, multi-layer를 이용하여 convolution 효과를 만들어, 연산량은 줄이고 깊은 네트워크로 직접 연결된 노드 뿐만 아니라 간접적으로 연결된 노드와의 관계적 특징 까지 추출할 수 있음
- GCN은 CNN과 매우 유사하다고 볼 수 있는데, 하나의 레이어가 shared weights를 이용해 필터와 비슷한 느낌으로 local connectivity를 학습하고 이는 곧 노드간의 관계적 특징을 추출한다고 볼 수 있고, 여기서 나온 아웃풋 임베딩을 다음 레이어에 활용함으로써 간접적으로 연결된 노드와의 관계적 특징 까지 추출한다고 볼 수 있음, 즉 multi-layer를 사용해 이웃노드와의 관계적 특징을 추출함
- MF 기반의 CF 모델들은 대부분 유저-아이템의 상호 작용을 내적으로 표현하여 임베딩을 학습시키기 때문에 유저와 아이템 임베딩 자체에는 상호 작용 정보가 들어있지 않다고 볼 수 있음
- 그러나 GNN은 유저-아이템의 상호 작용 정보를 임베딩에 포함하고, 해당 임베딩을 계속 전파시키면서 refine함으로써 Collaborative Signal을 명시적으로 임베딩 레이어에서 주입할 수 있음

## Session-based
- Session은 유저가 서비스를 이용하는 동안의 행동을 기록한 데이터
- 고객의 선호는 고정된 것이 아님, 예를 들어 어제와 오늘 고객이 좋아하는 아이템이 달라질 수 있고, 현재 핸드폰을 샀다면 유저에게 핸드폰을 추천해주어도 핸드폰을 구매할 확률을 매우 적을 것임
- 따라서 이처럼 고객의 행동 정보를 모델링 하는 것은 중요하고 이러한 고객의 행동 정보 데이터인 Session을 가지고 '지금' 고객이 좋아하는 것을 추천하는 방식이 바로 Session based Recommender System임

## Context-aware Recommendation
- Context-aware Recommendation은 유저와 아이템 간 상호작용 정보 뿐만 아니라, 맥락(context)적 정보도 함께 반영하는 추천 시스템임
- 유저 - 아이템 상호작용 정보를 사용하는 모델은 유저의 데모그래픽이나 아이템의 카테고리 및 태그 등 여러 특성(feature)들을 추천 시스템에 반영할 수 없다는 단점이 존재함
- 따라서 상호 작용 정보가 아직 부족한 아이템 또는 유저의 경우 추천을 할 수 없는 cold-start problem이 발생함
- 이에 유저와 아이템의 맥락적 정보(유저, 아이템 관련 정보)도 반영하며 모델링을 할 필요성이 증가하여 Context-aware Recommendation이 필요하다고 볼 수 있음
- 추천에서는 변수 간 상호 작용, 즉 아이템간 유저간 상호 작용을 모델에 반영하는 것이 핵심이기 때문에 Polynomial Model의 형태를 많이 사용함

## Factorization Machine
- sparse 한 입력 feature 상황에서도 각 feature의 잠재벡터를 학습하고 이를 기반으로 feature 간의 상호관계까지 모델링하여 예측하는 모델
- feature 사이의 상호관계를 나타내는 가중치를 직접 학습하는 것이 이나리 가중치를 분해하여 간접적으로 학습함
- sparse 한 입력 feature 상황에서는 feature 사이의 상호관계를 나타내는 가중치를 각 케이스별로 독립적으로 학습하기가 힘듬
- 이에 가중치를 분해하여 각 feature의 잠재벡터를 학습함으로써, 실제 데이터가 존재하지 않더라도 각 feature의 잠재벡터를 다른 상호관계로부터 학습할 수 있게 됨

## DeepFM
- DeepFM은 Factorization Machine을 사용하는 FM Component와 Deep Neural Network를 사용하는 Deep Component로 이루어진 모델암
- FM Component는 low-order feature interaction을 캡쳐하는데 강점을 보이는 부분으로(선형 결합), 기존의 FM 모델과 완전히 동일한 구조로 이루어짐
- Deep Component는 high-order feature interaction을 캡쳐하는데 강점을 보아는 부분으로(비선형 결합), 모든 feature들을 동일한 차원(k)의 임베딩으로 변환하고, 이 임베딩에 FM Component의 가중치와 동일하게 적용하여 hidden Layer의 인풋으로 사용함

## Multi-Armed Bandit
- Multi-Armed Bandit은 reward을 최대화 하기 위한 매 시간마다의 최선의 action을 Exploration과 Exploitation을 이용해 찾는 방법임
- Exploration(탐색)은 더 많은 정보를 얻기 위하여 새로운 arm을 선택하는 것을 말함
- Exploitation(활용)은 기존의 경험 혹은 관측 값을 토대로 가장 좋은 arm을 선택하는 것을 말함
- MAB의 Exploration과 Exploitation은 서로 Trade-off 관계를 가지기 때문에 적절하고 정밀한 Exploration과 Exploitation을 통해서 최대의 reward를 추정하는 것이 중요함
- MAB 알고리즘을 적절하게 사용하기 위해서는 확률이 수렴될 수 있을 만큼의 데이터를 수집해야 함
- 그런데 만약에 개인별로 Bandit을 구축한다면 수집되는 데이터의 수가 부족하여 MAB 알고리즘을 사용하기에 어려움
- 이에 비슷한 유저끼리 클러스터링 하여 그룹 내에서 Bandit을 구축하는 것이 효과적임

## Thompson Sampling
- Thompson Sampling은 주어진 k개의 action에 해당하는 확률 분포를 구하는 문제임
- 확률 분포는 베타 분포를 사용함. 왜냐하면 베타 분포는 알파, 베타 라는 두 상수에 의해 정해지는 함수인데, 여기서 두 상수 중 하나는 추천을 클릭한 횟수로, 하나는 추천을 클릭하지 않은 횟수로 정의하게 되면 추천을 클릭한 횟수와 추천을 클릭하지 않은 횟수 사이에 확률 분포를 알 수 있게됨
- 간단하게 설명하면 알파(추천을 클릭한 횟수)라는 값이 베타(추천을 클릭하지 않은 횟수)라는 값보다 커지게 되면 확률 분포에서 샘플링되는 값이 1에 가깝게 된다. 이에 다른 액션들보다 더 높은 값이 샘플링될 확률이 높아져 해당 action을 greedy action으로 선택할 수 있게 되는 것

## Cold-start-Problem
- 추천 시스템이 새로운 또는 어떤 유저들에 대한 충분한 정보가 수집된 상태가 아니라서 해당 유저들에게 적절한 제품을 추천해주지 못하는 문제를 말함
- 이를 해결하기 위해서는 아이템의 피쳐 정보를 바탕으로 추천을 해주는 content-based Model을 사용하거나, 초기 유저 정보를 수집하여 추천이 가능하게 하거나, 하이브리드 모델을 사용하여 추천을 해주는 방법 등이 존재함

## 참고 자료
- https://hongl.tistory.com/242
- https://velog.io/@2712qwer/series/Boostcamp-AI-Tech