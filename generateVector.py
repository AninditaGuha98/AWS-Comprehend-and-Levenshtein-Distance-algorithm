author = "Anindita"

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy
import pandas
import os


def createCSV(str1, str2, result):
    if (os.path.isfile('Levenshtein Distance.csv'))==False:
        mydict = {
            'current_word': str1,
            'next_word': str2,
            'distance': result
        }
        dataFrame = pandas.DataFrame(mydict, index=[0])
        dataFrame.to_csv('Levenshtein Distance.csv', mode='a', index=False)
    else:
        mydict = {
            'current_word': str1,
            'next_word': str2,
            'distance': result
        }
        dataFrame = pandas.DataFrame(mydict, index=[0])
        dataFrame.to_csv('Levenshtein Distance.csv', mode='a', index=False,header=False)


def levenshtein_distance(str1, str2):
    m = len(str1) + 1
    n = len(str2) + 1
    distance_matrix = numpy.zeros((m, n))

    for s1 in range(m):
        for s2 in range(n):
            distance_matrix[s1][0] = s1
            distance_matrix[0][s2] = s2

    # If last terminal alphabet is same then pick the diagonal element on left side, Minimum of left, up and diagonal element otherwise.
    for x in range(1, m):
        for y in range(1, n):
            if str1[x - 1] == str2[y - 1]:
                distance_matrix[x][y] = distance_matrix[x - 1][y - 1]

            else:
                distance_matrix[x][y] = 1 + min(distance_matrix[x][y - 1], distance_matrix[x - 1][y],
                                                distance_matrix[x - 1][y - 1])

    result = int(distance_matrix[m - 1][n - 1])
    print(str1, str2)
    print(result)
    createCSV(str1, str2, result)


stop_words_list = []
stopWords = set(stopwords.words('english'))
with open('001.txt') as f_read:
    text = f_read.read()
    content = text.split()
    for word in content:
        if word not in stopWords:
            stop_words_list.append(word)
        if len(stop_words_list) > 1:
            levenshtein_distance(stop_words_list[len(stop_words_list) - 1], stop_words_list[len(stop_words_list) - 2])

    print(stop_words_list)
