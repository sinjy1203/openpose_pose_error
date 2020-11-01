import cv2
import matplotlib.pyplot as plt
import copy
import numpy as np

from src import model
from src import util
from src.body import Body

body_estimation = Body('model/body_pose_model.pth') # 포즈 예측기, 인자: 학습 시킨 모델 파라미터 저장 경로
pose_compare = util.Pose_compare()                  # 내가 만든 모듈, 두개의 자세에서 오차를 알려줌

test_image1 = 'images/aa.jpg'                       # 비교할 이미지 1
test_image2 = 'images/dragon2.jpg'                  # 비교할 이미지 2

oriImg1 = cv2.imread(test_image1)                   # 이미지 불러오기
candidate1, subset1 = body_estimation(oriImg1)      # candidate: x, y, score, id | subset: index
                                                    # x와 y가 관절의 위치, index는 관절의 이름이라고 생각하면 됨
                                                    # score는 단순하게 확실 정도라고 보면됨
                                                    # id는 무시해도 되고

oriImg2 = cv2.imread(test_image2)                   # 이미지2 불러오기
candidate2, subset2 = body_estimation(oriImg2)

canvas1 = copy.deepcopy(oriImg1)                    # 이미지 복사
canvas1 = util.draw_bodypose(canvas1, candidate1, subset1)  # 화면에 예측한 스켈레톤을 보여줌

canvas2 = copy.deepcopy(oriImg2)
canvas2 = util.draw_bodypose(canvas2, candidate2, subset2)

mae = pose_compare.mae(candidate1, subset1, candidate2, subset2)    # 관절들의 위치를 통해 뼈의 각도를 알아내고
                                                                    # 두이미지의 각도의 mean average error를 구한다
print("자세 오류: ", mae)

plt.subplot(121)
plt.imshow(canvas1[:, :, [2, 1, 0]])
plt.axis('off')

plt.subplot(122)
plt.imshow(canvas2[:, :, [2, 1, 0]])
plt.axis('off')
plt.show()