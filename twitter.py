import tweepy, bow
import sys

# test
#print sys.argv[1] #username
username = sys.argv[1];
#print sys.argv[2] #profile
#pplType = sys.argv[2];


consumer_key = "5kKdB7HnZ2130eWP4ogl76iLt";
consumer_secret = "fZtdTXM5WSbmqfs4IQRC2TON8RFDHlsRjkzHiSDj2REba7QVrG";

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = "246855939-4mJXSxiYOh0A4xYoJyJFiVnBi2KP0cw3fu69XCGi";
access_token_secret = "WTk06KgTkTzNrz6Vc2UlMEZ31sheKTBaXrgnJx1XPF007";

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

listW = ['0']
bagTwit = bow.BagOfWords()

##### Retrieving tweets from this account

user_tweets = api.user_timeline(username)

for tweet in user_tweets:
	try:
		#print tweet.text
		for word in tweet.text.split():
			#print word + "=====\n"
			lineW = word.replace("?","").replace("!","").replace("@", "").replace("#", "").replace("$", "")
			#print "--"+lineW+"--" 
			bagTwit.add(str(lineW).lower());
	except:
		continue
		
rat = bagTwit.values()
wordshere =  bagTwit.items()
wkeys = bagTwit.keys()

#print rat
#print wordshere
#print "=================="
#print wkeys

def getKey(item):
	return item[1]
	
listSor = sorted(wordshere, key=getKey)
#print "=================="
#print listSor
#print max(rat)


################ Finding keywords 

col = 0
colList = []

happyWords = ['happy', 'yay', ':)', 'excited', 'awesome','love', 'happiness','laugh','lol', 'joy', 'rainbow', 'smile', 'won', 'congratulations', 'cheer', 'merry', 'grateful', 'glad', 'amazing', 'miracle', 'hope', 'gleeful', ':D']
sadWords = ['blue', 'down', 'sad', ':(', 'cry', 'lonely', 'terrorist', 'died', 'terror', 'evil', 'depression', 'sick', 'injury', 'reject', 'pain', 'dies', 'heartbreak', 'sorrow', 'hurts','worst', 'loser']
angryWords = ['mad', 'furious', 'hate', 'stupid', 'nerves', 'sick', 'tired', 'ruck', 'shit', 'damn', 'darn', 'bitch', 'asshole', 'dickhead', 'punish', 'rage','lies', 'blow up','arrogant','suck','payback','coward']
counterHappy = 0
counterSad = 0
counterAngry = 0

for i in xrange(len(listSor)):
	if listSor[i][col] is 'thanks':
		continue
	elif listSor[i][col] in happyWords :
		#print "Happyyyyy "+listSor[i][col]
		counterHappy += int(listSor[i][1])
	elif listSor[i][col] in sadWords:
		#print "Sad "+listSor[i][col]
		counterSad += int(listSor[i][1])
	elif listSor[i][col] in angryWords:
		#print "Angry "+listSor[i][col]
		counterAngry += int(listSor[i][1])
	else:
		colList += [ listSor[i][col] ]
#print colList
#print "HC ",counterHappy
#print "SC ", counterSad
#print "AC ", counterAngry


if counterAngry == counterHappy == counterSad:
	print "neutral";
elif counterHappy >= counterSad and counterHappy > counterAngry:
	print "happy";
elif counterSad > counterHappy and counterSad > counterAngry:
	print "sad";
elif counterAngry >= counterHappy and counterAngry >= counterSad:
	print "angry";
else:
	print "oops";
