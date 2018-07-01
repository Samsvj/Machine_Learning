#!/usr/bin/python3
import textblob
from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt 

def percentage(part,whole):
	return 100* float(part)/float(whole)

consumerKey= "********************" # Enter your consuemr_key here
consumerSecret= "***********************************************" # Enter your consuemr_secret here
accessToken= "***************************************************" # Enter your access_token here
accessTokenSecret= "************************************************" # Enter your access_token_secret here

auth = tweepy.OAuthHandler(consumerKey, consumerSecret) #setting up open_authorization by giving consumer key, consumer secret 
auth.set_access_token(accessToken, accessTokenSecret) # access token is the key to access Twitter API 
api=tweepy.API(auth)

searchTerm=input("Enter keyword/hashtag to search about: ")
noOfSearchTerms= int(input("Enter How many tweets to analyse: "))

tweets=tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfSearchTerms) #will scroll tweets about given hashtag upto the given number

#initializing all results to nill
positive=0
negative=0
neutral=0
polarity=0

for tweet in tweets:
	#print(tweet.text)
	analysis= TextBlob(tweet.text) #sentiment analysis via textblob 
	polarity += analysis.sentiment.polarity 
	print("reading tweet") 

	if(analysis.sentiment.polarity==0):
		neutral +=1

	elif (analysis.sentiment.polarity<0.00):
		negative +=1

	elif (analysis.sentiment.polarity>0.00):
		positive +=1

# calculating % based upon above results
positive=percentage(positive, noOfSearchTerms)
negative=percentage(negative, noOfSearchTerms)
neutral=percentage(neutral, noOfSearchTerms)


positive=format(positive,'.2f')
neutral=format(neutral,'.2f')
negative=format(negative,'.2f')

print("How people are reacting on " + searchTerm + "by analyzing" + str(noOfSearchTerms) + "Tweets.")

if (polarity==0):
	print("Neutral")
elif (polarity<0):
	print("Negative")
elif (polarity>0):
	print("positive")

# graphical representation of above results
labels=['Positive [' +str (positive)+'%]', 'Negative [' +str (negative)+'%]', 'Neutral [' +str (neutral)+'%]'] # labels on the graph

sizes= [positive, negative, neutral]

colors=['green', 'red', 'yellow']

patches, texts= plt.pie(sizes, colors=colors, startangle=90) #pie chart formation

plt.legend(patches, labels, loc="best")

plt.title('How people are reacting on ' + searchTerm +' by analyzing '+ str(noOfSearchTerms) +' Tweets.')

plt.axis('equal')

plt.tight_layout()

plt.show()
