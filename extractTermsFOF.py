from nltk import ngrams, FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from nltk.stem.snowball import SnowballStemmer

# extract technical terms from one file.

def  extractTechTerm(fileName ):
    #fileName="list.txt"
    stopwordFP=""
    with open('stopwordFP.txt') as f:
        for x in f:
            stopwordFP=stopwordFP+" "+x
    stopwordFP.strip()
    stopWords = set(stopwords.words('french')+stopwordFP.split())
    #print(stopWords)

    with open(fileName) as f:
        data = f.readlines()
    text=data[0].lower()
    text2=re.sub("[^A-Za-z áéèàçâêîôûëïü]+", ' ', text)
    text3=text2.strip()
    #print(text3)
    stemmer = SnowballStemmer("french")

    words = word_tokenize(text3,language='french')
    wordsFiltered = []

    for w in words:
        if w.lower() not in stopWords:
            wordsFiltered.append(w)


    all_counts = dict()

    sw=""
    s=[]
    for size in 1, 2, 3, 4, 5:
        all_counts[size] = FreqDist(ngrams(wordsFiltered ,size))
    size=0
    for size in 1, 2, 3, 4, 5:
        s=all_counts[size].most_common(int(50/size))#print(s)
        for e in s :
            word=""
            for w in e [0]:
                word=word+" "+w
            sw=sw+fileName[18:21]+";"+ word +";"+str(e[1])+"\n"
    print("size:"+str(size)+" "+sw)
    return sw
