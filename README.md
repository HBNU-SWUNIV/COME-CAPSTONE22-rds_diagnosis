# 한밭대학교 컴퓨터공학과 RDS_Diagnosis팀

**팀 구성**
- 20191752 장어진 (팀장)
- 20172614 조한용

## <u>Teamate</u> Project Background
- ### 필요성
  - RDS는 미숙아에게 흔하게 발생하며, 미숙아 사망 주요 원인 중 하나
  - 최근 고령산모, 시험관 시술 등의 이유로 미숙아와 조기 출산이 증가
  - RDS VS Non-RDS
    - RDS는 폐가 뿌옇게, Non-RDS는 X-ray 촬영시 검은 음영 형태로 나타남. 
 
- ### 기존 해결책의 문제점 <br>
  - 신생아는 아주 어리고 폐 영역이 작아 X-ray 영상의 일부만이 관심 영역
  - 신생아 특성상 관심 영역이 일관된 위치와 방향 X 
  - X-ray 영상에 다양한 기계 장치가 포함되어 영향을 미칠 수 있음
  
## System Design
  - ### System Requirements
    - 관심 영역을 분할하는 Semantic Segmentation 모델을 학습
    - 전문가가 정답으로 달아놓은 관심 영역을 바탕으로 분류 모델을 학습
    - 분할 모델 결과로 분류 모델을 재학습 시켜 최종 모델 생성
    - 시각화해서 의료 보조도구로서 활용할 수 있고 모델의 결과 분석 및 설명
    
## Case Study
  - ### 삽관 영역 제거에 따른 가중치 시각화 비교 <br>
  ![image](https://github.com/HBNU-SWUNIV/COME-CAPSTONE22-rds_diagnosis/blob/main/004%20Pictures/Compare_Visualize.png)
  
  - ### Overview 
  ![image](https://github.com/HBNU-SWUNIV/COME-CAPSTONE22-rds_diagnosis/blob/main/004%20Pictures/Overview.png)
  
  - ### 진단 프로그램 예시
  ![image](https://github.com/HBNU-SWUNIV/COME-CAPSTONE22-rds_diagnosis/blob/main/004%20Pictures/ex_program.png)

  
## Conclusion
- ### 경제적 & 사회적 효과
  - 전 세계 의료용 인공지능 시장은 2026년에 시장 규모가 450억 달러에 이르며, 연평균 40% 이상의 성장률을 보여 더 커지는 시장인 만큼 연구단계에서 끝나는 것이 아닌 실제 사업화를 진행할 수 있음
  - RDS는 미숙아 사망 주요 원인 1위인 만큼 심각한 문제인데 빠르고 정확한 진단하도록 우리의 모델이 도와줘 RDS로 고통받고 있는 미숙아에게 빠르고 적절한 치료가 가능해짐
- ### 기술적 효과
  - 신생아 질병 대상으로도 딥러닝 방식이 잘 작동하고 진단 보조 도구로서 사용가능함을 입증함
  
## Acknowledgement
- IRB 승인 받은 연구 결과물입니다. 
  
## Project Outcome
- ### 2022년 정보처리 춘계 학술대회 참가
- ### 한밭대학교 창의적 종합설계 경진대회 은상 수상
- ### K7U Belt 캡스톤 경진대회 장려상 수상
- ### 한밭대학교 정보기술대학 작품전시회 은상 수상 (총장상)
- ### Poster V1
![image](https://github.com/HBNU-SWUNIV/COME-CAPSTONE22-rds_diagnosis/blob/main/004%20Pictures/4.%20%ED%8C%90%EB%84%AC%EC%A0%9C%EC%9E%91%20%EC%96%91%EC%8B%9D_%EC%B5%9C%EC%A2%85_1.png)
- ### Poster V2
![image](https://github.com/HBNU-SWUNIV/COME-CAPSTONE22-rds_diagnosis/blob/main/004%20Pictures/%ED%95%99%EA%B3%BC%20%EC%9E%91%ED%92%88%EC%A0%84%EC%8B%9C%ED%9A%8C%20%ED%8F%AC%EC%8A%A4%ED%84%B0.png)
