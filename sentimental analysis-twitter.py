from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100*float(part)/float(whole)

consumerkey=""
consumersecret=""
accesstoken=""
accesstokensecret=""

auth=tweepy.OAuthHandler(consumerkey,consumersecret)
auth.set_access_token(accesstoken,accesstokensecret)
api=tweepy.API(auth)
searchTerm=input("Enter Keyword to search:- ")
no_of_terms=int(input("Enter how many tweets to analyse:- "))
tweets=tweepy.Cursor(api.search,q=searchTerm,lang="English").items(no_of_terms)

positive=0
negative=0
neutral=0
polarity=0

for tweet in tweets:
    analysis=TextBlob(tweet.text)
    #print(tweet.text)

polarity += analysis.sentiment.polarity

if(analysis.sentiment.polarity==0):
    neutral+=1
elif(analysis.sentiment.polarity<0.00):
    negative+=1
elif(analysis.sentiment.polarity>0.00):
    positive+=1


positive=percentage(positive,no_of_terms)
negative=percentage(negative,no_of_terms)
neutral=percentage(neutral,no_of_terms)
polarity=percentage(polarity,no_of_terms)

positive=format(positive,'.2f')
negative=format(negative,'.2f')
neutral=format(neutral,'.2f')

print("How people are reacting on "+searchTerm+" by analysing "+str(no_of_terms)+" Tweets.")

if(polarity==0):
    print("neutral")
elif(polarity<0.00):
    print("negative")
elif(polarity>0.00):
    print("positive")

labels=("Positive["+str(positive)+'%]', "Neutral["+str(neutral)+"%]", "Negative["+str(neutral)+"%]")
sizes=[positive,neutral,negative]
colors=['green','gold','red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("How people are reacting on "+searchTerm+" by analyzing "+str(no_of_terms)+" Tweets.")
plt.axis("equal")
plt.tight_layout()

plt.show()
