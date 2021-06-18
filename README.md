# 1. 시뮬레이터 상에서 DQN 학습

DQN을 이용해 학습시킨 뒤, 시뮬레이터 상에서 움직이기

- Learing DQN
- Python


## DQN
이 업무의 목표는 거리센서 정보를 사용할 수 있는 시뮬레이터에서, 강화 학습 DQN 기반으로 학습을 시켜서 자동차가 벽과 충돌하지 않고, 죽지 않고 살아남도록 만들기이다.

- [DQN](https://github.com/hyejeong99/Artificial-Intelligence/tree/master/DQN) - Learning with DQN 

## 코드 설명 

![untitled2](https://user-images.githubusercontent.com/59854960/113093629-41caf080-922b-11eb-8eec-f0d173b93bfd.png)

visdom으로 학습을 잘 진행하고 있는지 확인할 수 있다.
Loss는 감소하면서 0에 수렴하는 모습, Learning Curve는 증가하면서 100에 수렴하는 모습이 가장 이상적으로 잘 된 학습이라고 할 수 있다.

![untitled](https://user-images.githubusercontent.com/59854960/113093626-4099c380-922b-11eb-8b91-fdf5426472ff.png)

시뮬레이터에서 자동차가 잘 학습을 하고 있는지 확인할 수 있다.
리워드 값이 이전 리워드 값을 증가하면 동영상이 하나씩 만들어진다.

# 2. CNN 이용해서 차선 감지

이미지 데이터를 학습해 이미지를 보고 차선 감지하기.

- Learing CNN
- Python


## CNN(Enet-SAD)
Tusimple 데이터셋을 이용해 차선을 학습해줬다.
차선을 찾는데 6개 미만의 점이 나오는 차선이 있었다. 
이는 차선이 아닐 확률이 있으므로 제외시켜 줬다. 
polyfit을 이용해 차선 점을 이어 선을 그려줬다.

- [CNN](https://github.com/hyejeong99/Artificial-Intelligence/tree/master/CNN) - Recognize Car Lane

(1)참고 자료
https://github.com/InhwanBae/ENet-SAD_Pytorch

데이터셋 : Tusimple 

Enet-SAD 모델을 사용했고, Tusimple 데이터 세트로 훈련했다.

(2)요구 사항
pytorch, tensorflow, opencv
- train_gt.txt & val_gt.txt 파일 없다고 뜸 위의 파일 넣어주기

(3)결과
![결과](https://user-images.githubusercontent.com/59854960/115810918-bdcee780-a429-11eb-8a5a-591fdec6c5b1.png)


# 3. Lane Detect Viewer&Collector

머신러닝 전용 lane detect 모델 데이터 제작 프로그램과 뷰어 프로그램 병합한다.

- Machine Learning
- Python


## Lane Detect
data_collector.py = 차선에 점 찍는 파이썬 파일 data_viewer.py = 점 찍은 이미지 확인하는 파이썬 파일 
이 두 개의 파일을 하나로 합쳐서 하나의 파이썬 파일로 만든다.
점찍은 파일은 머신러닝 전용 lane detect 

- [Lane Detect](https://github.com/hyejeong99/Artificial-Intelligence/tree/master/Lane%20Detect) - Combine Programe

### 코드 설명
keyInput = input() 을 사용해서 키 입력에 따라 파일이 다르게 실행되도록 해주었다. 

- 키보드 1 입력 -> data_collector 실행 2
- 키보드 2 입력 -> data_viewer 실행 
- 그 외 키 입력 -> 예외처리

![0000000000](https://user-images.githubusercontent.com/59854960/113093045-1d224900-922a-11eb-8c43-eb1ff8bf484d.jpg)

다음과 같은 이미지 파일 차선에 점을 찍으면, polyfit으로 점을 이어준다.

# 4.CNN_example

"펭귄 브로의 3분 딥러닝 파이토치맛" 교제 코드

[3단원]

tensor_basic.py -> 3-1

tensor_operation.py -> 3-2

autograd_basic.py -> 3-3

image_recovery.py -> 3-4

basic_neural_network.py -> 3-5


[4단원]

fashion_mnist.py -> 4-1

neural_network.py  -> 4-2

overfitting_and_regularization.py -> 4-3


[5단원]

cnn.py -> 5-1

resnet.py -> 5-2

