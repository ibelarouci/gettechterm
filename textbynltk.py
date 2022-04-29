from nltk import ngrams, FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from nltk.stem.snowball import SnowballStemmer


stopwordFP=""
with open('stopwordFP.txt') as f:
    for x in f:
        stopwordFP=stopwordFP+" "+x
stopwordFP.strip()
stopWords = set(stopwords.words('french')+stopwordFP.split())
#print(stopWords)

with open('list.txt') as f:
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
        wordsFiltered.append(stemmer.stem(w))


all_counts = dict()



for size in 1, 2, 3, 4, 5:
    all_counts[size] = FreqDist(ngrams(wordsFiltered ,size))

s=all_counts[2].most_common(30)
print(s)
sw=""
for e in s :
    for e1 in e[0] :
        sw=sw+" "+e1
#print(sw)
