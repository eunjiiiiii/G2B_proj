# G2B_proj
공공조달 빅데이터 경진대회 프로젝트(4via)

---

1) 물품 영역의 적정 낙찰가 예측 서비스
2) 용역 영역의 적정 낙찰가 예측 서비스 
3) 유사도 산출을 통한 유사 입찰 공고 확인 서비스
4) 입찰 성공률 상승 도움 서비스

---

|개발환경|Python 3.8.5|
|---|---|
|사용 라이브러리|pandas 1.3.5, numpy 1.21.5, sklearn 0.23.2, matplotlib 3.3.2, pycaret 2.3.6, seaborn 0.11.2, pandasgui 0.2.13, scipy 1.4.1, Gower 0.05, lightgbm 3.3.2, xgboost 1.5.0, datetime, IPython, random|
|활용데이터(2021년)|물품 입찰공고내역, 물품 입찰분류별 진행 내역, 물품 입찰분류별 투찰업체 내역, 용역 입찰분류별 투찰업체 내역, 용역 입찰공고 내역, 용역 입찰분류별 진행 내역, 공사 입찰공고 및 진행내역, 공사 입찰공고별 투찰업체 내역|


(활용 데이터 출처 : 조달정보개방포털)

---

## 1. 물품 영역의 적정 낙찰가 예측 서비스
  ### 1) 데이터 전처리(물품모델_검증용.ipynb)
물품 입찰분류별 투찰내역, 물품 입찰공고 내역, 물품 입찰분류별 진행 내역 데이터의 공통변수인 입찰공고번호를      기준으로 inner join한 후 분석 진행
  ### 2) 모델링(물품_낙찰가예측모델.ipynb)
- pycaret AutoML 라이브러리 이용하여 성능이 좋은 상위 3개 모델 선택(LightGBM, XGBoost, RandomForest)
- GridSearchCV 모듈 사용하여 하이퍼파라미터 튜닝 후 비교

## 2. 용역 영역 적정 낙찰가 예측 서비스
  ### 1) 데이터 전처리(용역_전처리.ipynb)
용역 입찰분류별 투찰내역, 용역 입찰공고 내역, 용역 입찰분류별 진행 내역 데이터의 공통변수인 입찰공고번호를      기준으로 inner join한 후 분석 진행
  ### 2) 모델링(물품_낙찰가예측모델.ipynb)
- pycaret AutoML 라이브러리 이용하여 성능이 좋은 상위 3개 모델 선택(DecisionTree, RandomForest, Huber)
- GridSearchCV 모듈 사용하여 하이퍼파라미터 튜닝 후 비교

## 3. 유사도 이용한 이전 유사 입찰 공고 확인 서비스
  ### 1) 데이터 전처리(gower_preprocessing.ipynb)
입찰공고별 투찰업체 내역 중 실제 낙찰이 이루어진 데이터만 추출하여 분석
  ### 2) 모델링
Gower Similarit
  ### 3) 사용 예시(gower_similarity.py, gower_main.py)
  ### 4) 구체적 사용 예시
  ![pandas_gui](https://user-images.githubusercontent.com/47842737/197942580-c0e544ff-dd55-4cc1-84ee-260a181fb1ef.png)

  
## 4. 입찰 성공률 상승 도움 서비스
  ### 1) 데이터 전처리(경고서비스.ipynb)
물품입찰공고와 물품입찰분류별진행내역 데이터에서 입찰공고번호를 기준으로 inner join
  ### 2) 모델링(경고서비스.ipynb)

  
