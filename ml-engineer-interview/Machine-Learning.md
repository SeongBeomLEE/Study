# Machine Learning

## Confusion Matrix
- Confusion Matrix는 분류 모델의 성능 평가 지표를 계산하기 위해 활용되는 표임
- 이진 분류를 기준으로(0 - Negative, 1 - Positive) TP, FP, TN, FN으로 나눌 수 있음
- TP는 살제 Positive인 값을 모델이 Positive로 예측한 경우를 말함(제대로 예측)
- FP는 실제 Negative인 값을 모델이 Positive로 예측한 경우를 말함(잘못 예측)
- TN는 실제 Negative인 값을 모델이 Negative로 예측한 경우를 말함(제대로 예측)
- FN는 살제 Positive인 값을 모델이 Negative로 예측한 경우를 말함(잘못 예측)
- Accuracy는 모델이 얼마나 제대로 분류했는지를 나타내는 지표이기 때문에 (TP + TN) / (TP + FP + TN + FN) 로 계산할 수 있음
- Precision(Positive Predictive Value)는 예측 결과가 Positive일 때 실제 값도 Positive일 확률을 의미하는 지표이기 때문에 TP / (TP + FP) 로 계산할 수 있음
- Recall(True Positive Rate)는 실제 값이 Positive일 때 예측 결과도 Positive일 확률을 의미하는 지표이기 때문에 TP / (TP + FN) 로 계산할 수 있음
- Precision과 Recall은 서로 trade-off의 관계이기 때문에 1개의 값이 높아지면 반대의 값이 낮아지는 경향을 가짐
- 이에 Precision과 Recall의 조화 평균인 F1 score를 계산하여 불균형 데이터를 평가할 때의 지표로 사용하며 (2 * P * R) / (P + R)로 계산할 수 있음
- True Negative Rate(Specificity)는 실제 값이 Negative일 때 예측이 Negative인 비율을 말하기 때문에 TN / (TN + FP) 로 계산할 수 있음
- Negative Predictive Value는 예측 값이 Negative일 때 실제 값이 Negative인 비율을 말하기 때문에 TN / (TN + FN) 로 계산할 수 있음
- 따라서 Precision <-> Negative Predictive Value / Recall <-> Specificity 의 관계를 가짐

## ROC-curve
- ROC-curve는 다양한 threshold에 대한 이진분류기의 성능을 한번에 표시한 그래프임
- 모델을 이용해서 score 분포를 생성하고, 해당 score 분포를 실제 각 클래스에 대한 분포로 변환한 후에, 해당 분포가 서로 겹치는 부분이 적을수록 ROC-curve는 좌상단으로 밀착하게됨
- ROC-curve의 넓이를 계산한 지표를 AUC라고 부르며, ROC-curve는 좌상단으로 밀착했을 때 가장 좋은 성능을 보이고, 해당 ROC-curve의 AUC 값은 1에 가까워짐
- 따라서 이진 분류기의 성능이 랜덤이라면 ROC-curve는 단순히 대각선으로 표현되며, 이때의 AUC 값은 0.5임

## 경사하강법
- 주어진 목적 함수의 최솟값을 찾아가는 알고리즘으로, 목적 함수의 기울기와 학습률을 곱하여 파라미터에 -를 해줌으로써 파라미터를 업데이트 해나감
- 경사하강법이 가능한 이유는 목적 함수의 최솟 값에 가까워질수록 미분 계수, 즉 기울기의 값이 작아지기 때문에 학습률만 잘 설정한다면 최솟값에 가까워질 수 있는 것임
- 그리고 이 경사하강법에서 우리는 인풋데이터를 정규화하는 이유를 알 수 있음, 기울기를 구할 때 에러와 인풋 데이터를 같이 곱하고 그 값의 평균을 사용하는데 우리는 여기서 기울기의 값이 너무 커지면 그 밧이 발산한다는 것을 알고 있음, 따라서 기울기의 발산을 최대한 막고자 인풋데이터를 정규화하는 것이라고 할 수 있음
- 목적 함수의 모양이 convex가 아닌 경우 global minimum이 아닌 local minimum으로 수렴할 수 있음
- 학습률이 너무 크다면 최솟값이 아니라 발산할 수 있음
- 학습률이 너무 작다면 수렴하는 속도가 매우 느릴 수 있음

## Linear Regression
- 선형 회귀는 회귀 문제를 풀기 위한 알고리즘으로 현재 주어진 데이터를 가장 잘 설명할 수 있는 하나의 선을 찾는 방식이라고 할 수 있음
- 이 선을 찾는 방식에는 정규방정식, 경사하강법 등이 있는데 우리는 대부분 경사하강법을 이용하여 파라미터를 추정함
- 경사하강법을 이용하여 목적 함수가 최소가 되는 직선을 찾아나감
- 목적 함수가 최소가 되는 직선이 곧 오차가 최소가 되는 지점임
- 이 밖에 회귀 분석을 위한 가정은 확률과 통계의 회귀 분석 파트를 보면 좋음

## Logistic Regression
- 로지스틱 회귀는 이진 분류 문제를 풀기 위한 알고리즘임
- 선형 회귀 식에 sigmoid 함수를 적용하고 binary cross entropy loss를 계산하여 해당 데이터를 가장 잘 분류할 수 있는 파라미터를 경사하강법을 이용해 찾아나감

## SVM
- SVM은 Support Vector와 결정 경계 사이의 최대 마진을 갖게 하는 알고리즘임
- 즉, 최적의 Support Vector를 찾아내어 최대의 마진을 가질 수 있게 하는 결정 경계를 찾으면 되기 때문에 속도는 매우 빠르다고 할 수 있음
- 파라미터인 C를 통하여 마진 사이에 어느 정도의 데이터를 무시할지 정할 수 있음(C값이 클수록 하드마진(오류 허용 안 함), 작을수록 소프트마진(오류를 허용함))
- SVM은 분류에 사용되는 지도학습 머신러닝 모델이다.
- SVM은 서포트 벡터(support vectors)를 사용해서 결정 경계(Decision Boundary)를 정의하고, 분류되지 않은 점을 해당 결정 경계와 비교해서 분류한다.
- 서포트 벡터(support vectors)는 결정 경계에 가장 가까운 각 클래스의 점들이다.
- 서포트 벡터와 결정 경계 사이의 거리를 마진(margin)이라고 한다.
- SVM은 허용 가능한 오류 범위 내에서 가능한 최대 마진을 만들려고 한다.
- 파라미터 C는 허용되는 오류 양을 조절한다. C 값이 클수록 오류를 덜 허용하며 이를 하드 마진(hard margin)이라 부른다. 반대로 C 값이 작을수록 오류를 더 많이 허용해서 소프트 마진(soft margin)을 만든다.
- SVM에서는 선형으로 분리할 수 없는 점들을 분류하기 위해 커널(kernel)을 사용한다.
- 커널(kernel)은 원래 가지고 있는 데이터를 더 높은 차원의 데이터로 변환한다. 2차원의 점으로 나타낼 수 있는 데이터를 다항식(polynomial) 커널은 3차원으로, RBF 커널은 점을 무한한 차원으로 변환한다.
- RBF 커널에는 파라미터 감마(gamma)가 있다. 감마가 너무 크면 학습 데이터에 너무 의존해서 오버피팅이 발생할 수 있다.

## 앙상블
- 앙상블 학습은 여러 개의 모델을 결합하여 하나의 모델보다 더 좋은 성능을 내는 머신러닝 기법
- 앙상블 학습의 핵심은 여러 개의 약 분류기(Weak Classifier)를 결합하여 강 분류기(Strong 
Classifier)로 만드는 것
- 앞면(정답)이 51%, 뒷면(오답)이 49%가 나오는 동전이 있다고 가정했을 때, 시행 횟수가 많아지면 많아질 수록 앞면이 다수가 될 확률이 높아짐
- 여기서 시행 횟수를 모델의 개수로 앞면이 다수가 될 확률을 앙상블 모형의 정확도로 본다면, 앙상블이 왜 좋은 성능을 보여주는 것인지 유추할 수 있음

## Decision Tree
- Decision Tree는 나무가 뿌리를 내리듯이 여러 변수간의 조합을 바탕으로 엔트로피가 최소가 되는 조건을 찾고, 해당 조건을 기준으로 계속 분기하면서 최적의 모델을 학습시키는 알고리즘
- Decision Tree는 분산과 편향을 조절하기 쉽기 때문에 앙상블의 Base Model로 많이 쓰임(모델의 깊이를 깊게 하면 분산이 높아지고, 모델의 깊이를 얖게 하면 편향이 높아짐)
- 분산은 예측의 변동폭이 얼마나 큰지를 반영, 편향은 예측이 정답에서 얼마나 떨어져 있는지를 반영

## 배깅과 부스팅
- 배깅은 Bootstrap Aggregating의 줄임말로 Bootstrap의 Subset Sample로 동일한 모델 N개를 학습하여 앙상블하는 방법임
- 다양한 Sampling Dataset을 만드는 방법이 바로 Bootstrapping이고, Bootstrapping을 활용하여 다양한 Classifier을 만드는 방법이 바로 Bagging임
- Bootstrapping은 중복을 허용하여 데이터를 샘플링하는 방법(복원 추출)
- Bootstrapping을 통하여 데이터 셋을 추출하면 전체 데이터의 63%만 샘플링 됨
- 샘플링이 되지 않은 37% Data를 OOB 샘플이라고 하며, 해당 샘플을 이용하여 모델의 성능을 평가함
- 배깅은 여러 개의 모델이 서로 다른 데이터셋으로 학습하기 때문에 독립적으로 학습됨
- 반대로 부스팅은 여러 개의 모델이 연속적으로 학습함
- 부스팅은 가중치를 활용하여 약 분류기(High Bias Model)를 강 분류기로 만드는 방법
- 잘못 분류된 데이터에 가중치를 부여하여 학습이 진행됨에 따라서 더 잘 분류해보는 것이 목적임
- 흔히 배깅은 모델의 분산응 줄이는 방법이고, 부스팅은 모델의 편향을 줄이는 방법이라고 함

## RandomForest
- Bagging 방식을 활용한 Decision Tree Base의 대표적인 Ensemble Model이 RandomForest임
- Bagging과 Randomized Decision Tree를 결합한 방식으로 볼 수 있음
- Bootstrap을 바탕으로 다양한 데이터 셋을 만들고, 각 데이터셋을 이용하여 DT 모델을 사용하는데, 활용 변수도 랜덤하게 선택함
- 이렇게 여러개의 DT를 병렬적(독립적)으로 학습하여 앙상블 하는 것이 바로 RandomForest임
- 즉 DT를 Bagging 방식으로 앙상블 한 것이 바로 RandomForest라고 할 수 있음(과적합된 Tree를 앙상블하자)

## AdaBoost
- AdaBoost는 오분류된 데이터를 더 잘 맞추는 모델을 연속적으로 만드는 것이 목표인 모델
- 방법은 오분류된 데이터의 가중치를 높여서, 오분류된 데이터가 학습에 더 자주 포함되게 만드는 것
- 약 분류기로 stump(depth가 1인 매우 작은 DT)를 사용하고, 학습 시에 매 Round마다 Observation의 Weight 값을 계산하고, 틀리는 Observation의 Weight를 Up 시켜서, 잘못 분류된 데이터를 더 잘 맞추게 하는 방법이 바로 AdaBoost임
- 즉 DT를 부스팅 방식으로 앙상블 한 것이 바로 AdaBoost라고 할 수 있음(과소적합된 Tree를 앙상블하자)

## Gradient Boosting
- AdaBoost는 이전 모델의 단점을 데이터에서 찾는 방식이라면, Gradient Boosting은 모델의 예측 값을 바탕으로 데이터의 잔여 오차(residual error)를 계산하여 이를 연속적으로 게속 예측하는 방식으로 모델을 학습시키는 방식임
- 모델 학습 방법이 Gradient Descent 알고리즘을 활용하여 Gradient Boosting이라고 불림
- 매 Round마다 잔여 오차(residual error)값을 계산하고 Residual을 가지고 Model을 학습하고 전에 학습된 모델의 오차를 보완하는 방향으로 모델이 학습됨

## 참고 자료
- https://angeloyeo.github.io/
- https://icim.nims.re.kr/post/easyMath
- https://hleecaster.com/ml-svm-concept/