author= "Anindita"


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words_list=[]
stopWords= set(stopwords.words('english'))
with open('001.txt') as f_read:
    text=f_read.read()
    content=text.split()
    for word in content:
        if word not in stopWords:
            stop_words_list.append(word)
    print(stop_words_list)

