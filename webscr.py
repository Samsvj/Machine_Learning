from bs4 import BeautifulSoup
import urllib.request as ureq
import nltk
from nltk.book import *
from nltk.corpus import stopwords
import matplotlib.pyplot as plt 
import string

#reading data from url 
url=ureq.urlopen('https://github.com/redashu')
#print html tagged data 
print (url.read)
webdata=url.read()

#applying soup #html parsing 
souped_data=BeautifulSoup(webdata,'html5lib')
print (souped_data)

#only text extraction 
text_data= souped_data.get_text()
print(text_data)

#tokenize process on behalf of words
tokenized = [i for i in text_data.split() if i.lower() not in stopwords.words('english')]
print(tokenized) 

#calculating wordcount
wordcount=nltk.FreqDist(tokenized)
print ('wordcount')

#removing punctutaion marks 
words=[word for word in tokenized if word.isalpha()]
print (words[:15])

for word, frequency in wordcount.most_common(50):
   print(u'{};   {}'.format(word, frequency))
    
#plotting a graph of frequency of words 
wordcount.plot(25)
#separating positive tags
pos=nltk.pos_tag(tokenized[10])
print (pos)



