################################################
# nltk parser를 이용하기 위해 참고한 자료
################################################
# https://blog.manash.me/configuring-stanford-parser-and-stanford-ner-tagger-with-nltk-in-python-on-windows-f685483c374a
# https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software
# https://gist.github.com/alvations/e1df0ba227e542955a8a

# 더이상 nltk 툴킷에서 제공하지 않음...
# https://stackoverflow.com/questions/13883277/stanford-parser-and-nltk

# 구글에서 발표한 syntaxnet이 가장 성능은 좋다만, 당장 쓰기엔 어려움
# https://research.googleblog.com/2016/05/announcing-syntaxnet-worlds-most.html
# 위 링크 구글의 논문
# https://arxiv.org/pdf/1603.06042v2.pdf

# 유명한 parser: stanford, berkeley, Google-SyntaxNet, pattern, ... 영문 parser는 정말 많이 있음
# malt parser, dependency 같은 개념을 가진 parser도 공부해야 사용할 때 이해가 잘 될듯함
# nltk에서 malt parser 사용하는 방법
# https://stackoverflow.com/questions/14009330/how-to-use-malt-parser-in-python-nltk
# nltk에서 SyntaxNet 사용하는 방법
# http://www.davidsbatista.net/blog/2017/03/25/syntaxnet/



################################################
# 해야되는 사향
################################################
# java 환경 변수 설정, nltk tool 환경변수 설정(CLASSPATH, STANFORD_MODEL)
# englishPCFG.ser.gz 및 stanford-english-corenlp-2017-06-09-models.jar 경로에 넣어주기



################################################
# 영문 parsing 예시
################################################
# 나중에 dependency를 공부하고 난 뒤에는 이것을 사용해보자
# from nltk.parse.stanford import StanfordDependencyParser
# parser = StanfordDependencyParser(model_path="C:\\Users\\DeokseongSeo\\Anaconda3\\Lib\\site-packages\\stanford_tools\\stanford-parser-full-2017-06-09\\englishPCFG.ser.gz")


#예문
sentence = "The pedal is not wide enough"

#parsing tree 만들기
from nltk.parse.stanford import StanfordParser
parser = StanfordParser(model_path="C:\\Users\\DeokseongSeo\\Anaconda3\\Lib\\site-packages\\stanford_tools\\stanford-parser-full-2017-06-09\\englishPCFG.ser.gz")
parsed_tree = list(parser.raw_parse(sentence))
print(parsed_tree)

#parsing tree 시각화
for line in parsed_tree:
    for sentence in line:
        sentence.draw()


