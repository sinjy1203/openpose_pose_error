# 홈트장인
>집에서도 사용자가 전문가의 요가동작을 따라해보고 피드백을 받을 수 있는 앱 제작  

</br>

## 1. 제작 기간 & 참여 인원
- 2020년 3월 ~ 2020년 11월
- 팀프로젝트 (팀원 3명)

</br>

## 2. 역할
사용자와 전문가의 요가동작을 비교하고 유사성을 수치화하는 역할

</br>

## 3. 사용 기술
- python
- opencv
- pytorch
- openpose

</br>

## 4. file 설명
### 'main.py' 
- main 실행 코드, 두 이미지를 openpose를 통해 스켈레톤 값을 얻고 관절 각도를 비교해 mae값을 리턴
- https://github.com/sinjy1203/openpose_pose_error/blob/master/main.py
### 'src/util/Pose_compare' 
- 스켈레톤 값을 이용해 관절각도를 리턴, 관절각도들을 비교해 mae값 리턴
- https://github.com/sinjy1203/openpose_pose_error/blob/master/src/util.py

https://github.com/Hzzone/pytorch-openpose 사용

</br>

## 5. 트러블 슈팅
### 신장차이에 따른 비교 문제
- 처음에 비교할 두 이미지 각각의 스켈레톤 값을 비교하였더니 올바르게 동작을 취해도 신장차이에 따른 차이가 발생하였습니다. 
- 또한 같은 사람이 같은 동작을 취해도 카메라 각도에 따라서 차이가 발생하였습니다.
- 이를 해결하기 위해 스켈레톤 결과값을 모두 이용하는 것이 아니라 관절 각도를 이용해서 동작의 차이를 수치화하였습니다.
