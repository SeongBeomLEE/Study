# Deep Learning

## local minimum과 global minimum
- 해당 위치의 기울기가 0이며, 해당 위치의 주변보다 작은 값을 가지는 점을 local minimum 이라고 부름
- 이 local minimum들 중에서 가장 작은 값을 가지는 점을 global minimum이라고 부름

## Optimazor
- Optimazor는 경사하강법을 적용할 때 가중치를 조정시켜주는 알고리즘임
- Optimazor는 크게 learning rate를 고정시키는 non-adaptive learning rate 방식과 학습을 진행하면서 learning rate 값을 조정해나가는 adaptive learning rate 방식으로 나뉘어짐
- non-adaptive learning rate 방식의 대표적인 알고리즘은 SGD와 Momentum임
- SGD는 전체 데이터셋이 아닌 일부 샘플 데이터셋을 만들어 경사하강법을 진행하는 방식으로, 샘플 데이터셋으로 계산을 하기 때문에 계산 속도가 매우 빠르며, 다양한 샘플 데이터를 바탕으로 모델을 학습시키기 때문에 조금 더 다양한 함수를 근사화 할 수 있어 GD 보다 global minimum에 수렴할 가능성이 조금 더 높아짐
- Momentum은 SGD와 달리 이전 스템의 기울기 정보들을 사용하여, 현재의 진행 방향에 대한 관성을 부여하여 샌들포인트에서 조금더 잘 빠져나올 수 있도록 만들어준 알고리즘임
- adaptive learning rate 방식의 대표적인 알고리즘은 RMSProp과 Adam임
- RMSProp은 학습을 진행할수록 learning rate 값을 조정해나가며 좀 더 섬세하게 global minima를 찾아갈 수 있도록 해줌
- Adam은 RMSProp과 모멘텀을 결합한 기법으로 모멘텀처럼 관성의 법칙을 부여하고 RMSProp의 adaptive learning rate 방식을 결합한 방식임

## Batch Norm
- Covariate shift는 공변량 변화라고 부르며 입력 데이터의 분포가 학습할 때와 테스트할 때 다르게 나타나는 현상을 말함
- Covariate Shift(공변량 변화)가 뉴럴 네트워크 내부에서 일어나는 현상을 Internal Covariate Shift라고 함
- hidden layer를 통과하면 통과할수록 데이터의 분포가 달라지는 Internal Covariate Shift 문제가 발생하여 이를 해결하기 위해 나온 기법이 Batch Norm임
- Batch Norm은 레이어마다 특정 trainable parameter인 감마와 베타를 두어 데이터의 특성에 맞추어 feature 별로 정규화를 수행하는 기법임
- 이 덕분에 데이터의 분포를 계속해서 유지해줌으로써 gradient smoothing 효과로 비교적 모델이 global minima에 더욱 빠르게 수렴할 수 있도록 도움을 줌
- 그러나 feature에 계속된 변형을 가하므로, 원래 데이터가 가지고 있던 특성이 사라진다는 단점이 있음
- 그런데 Batch Norm에 대한 다른 의견으로는 Batch Norm은 Internal Covariate Shift를 해결해주는 것이 아니라, 단순히 기울기의 범위를 일정하게 유지해주기 때문에 (기울기의 크기를 적절하게 유지시켜줌) 성능이 좋은 것이라고 말하는 논문도 있음

## Embedding 이란?
- Embedding은 주어진 데이터를 낮은 차원의 벡터(vector)로 만들어서 표현하는 방법
- Embedding 방법은 크게 Sparse Representation과 Dense Representation으로 나뉨
- Sparse Representation은 one-hot encoding 등과 같이 표현하려는 데이터의 수와 차원의 수가 동일한 Representation 방법으로, 데이터의 수가 많아질수록 벡터의 차원이 한없이 커지고 공간의 낭비가 발생함
- Dense Representation은 Word2Vec 등과 같이 표현하려는 데이터의 수보다 훨씬 작은 차원으로 나타내는 Representation 방법으로, 공간의 낭비가 발생하지 않는다는 장점이 존재하나 차원 자체가 하이퍼 파라미터이기 때문에 적절한 조정이 핑요함

## MLP
- 완전 연결층으로 이루어진 선형모델과 활성화함수를 이루어진 Layer가 deep 하게 이루어진 모델

## CNN
- CNN은 Convolution Layer를 기반으로 이미지 분야에 대하여 좋은 성능을 보여주는 모델임
- 이미지 분야에서 좋은 성능을 보이기 위해서는 위치적 특징을 잘 캡쳐할 수 있어야함
- 위치적 특징을 잘 캡쳐하기 위해서 CNN은 필터, 스트라이드, 패딩, 풀링의 개념을 활용함
- 필터는 스트라이드의 크기 만큼 이미지를 순회하면서 이미지의 특징을 추출함
- 해당 필터는 가중치가 공유됨에 따라서 위치 불변의 지역적 특징을 더욱더 잘 캡쳐할 수 있게 됨
- 패딩을 통해서 필터로 생성된 피쳐 맵의 크기를 조절할 수 있으며, 이미지의 모서리 부분의 특징을 추출할 수 있도록 도와줌
- 풀링을 통해서 이미지의 가장 중요한 특징만을 뽑아내는 맥스풀링 등을 이용해 이미지의 크기를 조절할 수 있음
- CNN의 경우 high-level feuture를 추출할 수 있어야 하는데, 이를 위해서는 receptive field를 넓혀야 함
- receptive field를 넓히는 방법은 필터의 크기를 키우거나, 모델의 깊이를 깊게 해야함
- 필터의 크기를 키우면 그만큼 파라미터의 수가 늘어나 매우 비효율 적임(왜? 5x5 2개 쌓는 방식 보다 3x3 3개를 쌓는 방식이 파라미터의 수는 적으면서 receptive field를 동일하게 가져갈 수 있음)
- 그래서 대부분 3x3 필터를 이용하고 모델의 깊이를 깊게 하는 방식으로 모델을 쌓아나감
- 그런데 단순히 모델의 깊이를 깊게 쌓으면 성능이 떨어지는 문제점이 발생했고, 이에 residual block이라는 새로운 기법이 탄생했고, 이 덕분에 CNN은 성능 하락 없이 모델을 더 깊이 쌓을 수 있게됨

## RNN
- RNN은 각 히든 레이어가 순차적으로 연결되어 있어 input으로 이전 스텝의 hidden state를 계속해서 사용하는 것이 가장 큰 특징인 모델임
- 이러한 순차 학습의 장점 덕분에 이전 데이터의 정보를 활용하는 것이 중요한 시계열 데이터에 적합한 방법임
- 그런데 RNN에 자체가 순차적으로 연결되어 있어서 역전파를 진행할 시에 멀리있는 히든 레이어까지 기울기가 제대로 전달되지 못한다는 단점이 존재함
- 이 때문에 특정 히든 레이어 기준으로 최근 데이터가 더 강하게 학습되고 레이어가 깊어지면 깊어질수록 과거 데이터가 희미해진다는 단점이 존재함
- 이에 RNN은 시계열 데이터의 그 길이가 짧을 때 사용하는 것이 좋음
- https://techblog-history-younghunjo1.tistory.com/481

## LSTM
- LSTM은 gate의 개념을 부여하여 특정 게이트는 최근 정보를 학습하고 다른 게이트는 과거 데이터를 위주로 학습하게 하여 기존의 RNN에서 발생했던 오래된 정보는 기억하지 못한다는 문제점을 해결한 기법임
- RNN은 역전파 계산시에 곱셈만을 사용했다면, LSTM은 곱셈과 덧셈의 연산을 적절히 사용하여 멀리 있는 레이어 까지 기울기가 전달될 수 있도록 구조를 만듬
- 그런데 복잡한 구조 때문에 파라미터의 수가 RNN 보다 많아서 계산 복잡도가 크다는 것이 단점임

## GRU
- GRU는 LSTM에서 가장 핵심적인 Gate만 가져와서 LSTM 보다 파라미터의 수를 줄인 방법임

## Transformer
- Transformer는 RNN과 달리 입력 데이터를 병렬적으로 학습한다는 것이 가장 큰 특징인 모델
- Transformer는 self-attension의 개념이 적용되어 학습 시에 입력 시퀀스가 유의미하게 순차적으로 연결이 되어 있지 않아도 필요한 부분에만 집중하여 컨텍스트 벡터를 생성할 수 있고, 모델이 병렬적으로 학습을 하기 때문에 속도가 빠르다는 장점이 존재
- 하지만 모든 문장의 정보를 담은 하나의 Context Vector를 생성하기 어렵고, 모델이 병렬적으로 학습을 하여 inductive-bias가 낮아져 대부분의 경우 많은 양의 데이터를 필요로 한다는 단점이 존재