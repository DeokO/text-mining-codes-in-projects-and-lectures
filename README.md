# text-mining-codes-in-projects-and-lectures
text mining codes (POS-tagging, embedding, parsing, modeling ...)

-----------------------------------------------------------

## 01_2017spring_Pattern Recognition lecture team project
* 2017년 1학기 고려대학교 뇌공학과 석흥일 교수님의 패턴인식 수업에서 팀프로젝트로 사용한 코드입니다.
* code
  * 01_make_inputdata.py: 
    - input data에 대해 전처리(tokenization, lemmatize, stopwords elimination)
    - 데이터셋 구성(TF-IDF, LDA의 문서당 토픽의 분포, Doc2Vec)
  * 02_model.py: 분류모형 적합(Naïve Bayesian, Decision Tree, simple Ensemble) 및 성능 비교
* data
  * input data: 
    - economic_news_article
    - ohsumed (용량 문제로 압축해서 업로드)
    - reuter
  * TOTAL: output이 저장될 폴더. 코드를 돌리면 이 폴더에 output이 저장된다.
* document
  * [Team 5]_Final_Report.pdf: 최종 과제 결과물로 제출한 파일

## 02_nltk_parser
* nltk_parsingTree_visualize.py
* nltk에서 제공하는 Stanford parser를 이용하기 위한 코드입니다.
* 이것을 사용하기 위해서는 다운받을 것들과 설정할 사항이 많습니다.
  * java 환경 변수 설정, nltk tool 환경변수 설정(CLASSPATH, STANFORD_MODEL)
  * englishPCFG.ser.gz 및 stanford-english-corenlp-2017-06-09-models.jar 경로에 넣어주기
* nltk에서 제공하는 paser로 stanford의 parser를 이용한 예시 코드이며, 다른 여러 parser들도 연습해 볼 계획입니다.
* 제일 아래에는 parsing tree를 시각화해서 보는 부분이 있습니다.


