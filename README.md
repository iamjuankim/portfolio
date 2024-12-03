# portfolio
portfolio 폴더에는 제가 지금까지 진행한 Python, R 프로젝트의 파일이 첨부되어 있습니다. 

**1. Crawling**
   
   크롤링과 관련해 진행한 여러가지 활동입니다.
   **crawling.py**: 파이썬을 활용하여 네이버에 특정 검색어를 입력했을 때 **상단에 노출되는 기사 제목을 크롤링**하는 소스코드. 
   
   **워드클라우드.py**: 크리스마스와 관련된 포털 키워드를 크롤링하여 트리 형태의 워드클라우드를 제작해주는 소스코드. tree.png 파일로 결과물 샘플을 확인할 수 있습니다.


**2. R**

   **R**을 활용해 **빅데이터 분석**을 수행하였습니다. 
   학생 1000명의 거주 지역, 희망 진로 분야, 과외 학습 시간 등이 나와있는 education.dat파일을 R을 활용해 **평균, 중앙값, IQR과 같은 통계량을 구해** 분석하였습니다. 추가로 **히스토그램, Side-by-Side Bar Chart (막대그래프), 산점도를 그려 자료를 시각화**하였습니다. 


**3. ImageSorter**
   
   Python의 **Tensorflow 라이브러리**를 이용해 사진을 업로드하면 **실질적 화질을 분석하고 압축해주어 용량을 줄여주는 프로그램**을 개발하는 프로젝트이며, 현재 진행 중입니다. 
   
   **img_create.py**: 화소별로 50장씩 준비된 2560 x 1440 크기의 이미지 데이터에서 **20개의 32 x 32 이미지를 잘라낸 뒤, 이미지 크기를 10배 늘려주는 (scale-up) 소스코드**입니다. 이렇게 생성된 1000장의 사진을 활용하여 지도학습에 기반해 모델을 학습시켰습니다. 
   
   **img_split.py**: overfitting을 방지하기 위해 데이터의 80%를 모델 학습에, 20%를 검증에 사용하였습니다. **화소별 1000장의 사진을 정해진 비율에 따라 랜덤하게 test 폴더와 train 폴더에 분류해 이동시켜주는 소스코드**입니다. 
   
   **img_sort.py**: 7000장의 사진을 통해 CNN(합성곱신경망)으로 모델을 학습시키고, 최종적으로 keras 파일의 형태로 저장해주는 소스코드입니다. 픽셀 정보를 보존하기 위해 Data Augmentation에는 좌우상하 반전만을 사용하였으며, Epoch(에포크)는 10으로 설정했습니다. 


**4. Connect4**

   4목 형태의 유명 게임 Connect4를 파이썬을 활용해 제작하였습니다. 다양한 반복문을 활용해 두명의 플레이어가 번갈아가며 원하는 칸을 선택해 게임을 진행할 수 있게끔 했습니다. 



# Portfolio

This repository showcases the projects I have worked on using Python and R. Each project highlights specific skills and methodologies I have developed during my learning journey.

## 1. R

Conducted big data analysis using R.
- **education.dat**: Dataset containing information about 1,000 students, including their residential areas, desired career fields, and hours spent on private tutoring.
- **Analysis**:
  - Calculated statistical measures such as the mean, median, and interquartile range (IQR).
  - Visualized data using histograms, side-by-side bar charts, and scatter plots.

---

## 2. ImageSorter

A project utilizing Python's TensorFlow library to analyze the actual quality of uploaded images and compress them to reduce file size.

### Files:
- **img_create.py**:
  - Crops 20 32x32 images from pre-prepared 2560x1440 image data (50 images per resolution).
  - Scales cropped images up by a factor of 10 to create a dataset of 1,000 images for supervised learning.
- **img_split.py**:
  - Splits the dataset into 80% for training and 20% for validation to prevent overfitting.
  - Randomly divides 1,000 images per resolution into `train` and `test` folders.
- **img_sort.py**:
  - Trains a Convolutional Neural Network (CNN) model with 7,000 images.
  - Saves the trained model in Keras format.
  - Uses only basic data augmentations (horizontal and vertical flipping) to preserve pixel integrity.
  - Sets the Epoch to 10 for training.

---

## 3. Crawling

Various projects related to web crawling using Python.

### Files:
- **crawling.py**:
  - A script that scrapes the titles of top articles displayed on Naver when a specific search term is entered.
- **wordcloud.py**:
  - Generates a tree-shaped word cloud from portal keywords related to Christmas.
  - Sample output: `tree.png`.

---

## 4. Connect4

A Python implementation of the classic Connect4 game.
- Enables two players to take turns selecting cells using various loops.

---

Feel free to explore the projects, and let me know if you have any questions or feedback!
