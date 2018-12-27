# Reddit libaries
import praw



# Machine learning libaries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Initalizing Reddit object which we will use to interact with the site
reddit = praw.Reddit(
    client_id = '2D96SxaOxD31IQ',
    client_secret = 'KyPYwaOWiMdfWXZauI1of_BmLu0',
    user_agent = 'what am i doing' # Name your user agent whatever you like
)

# If this prints, then you have successfully interacted with Reddit
if reddit.read_only:
    print("Log: Contact with Reddit has been established")
else:
    print("Log: Contact with Reddit has FAILED")


# Collect top 10 submissions from UWaterloo as a list
uw_submissions = list(reddit.subreddit('uwaterloo').hot(limit=10))

# Find one single TOP submission from the list. It has certain parameters like comments and title underneath it.
top_uw_submission = uw_submissions[4]

# Provide the comments of the submission as a list
uw_comments = top_uw_submission.comments.list()




# Perform the same as above
uoft_submissions = list(reddit.subreddit('uoft').hot(limit=10))

# Same as above
top_uoft_submission = uoft_submissions[4]

#same as Above
uoft_comments = top_uoft_submission.comments.list()




# Get the comment text for each comment in the UW one and the UofT one
corpus = [comment.body for comment in (uw_comments[:5] + uoft_comments[:5])]
# Label which comments are UW and which are UofT comments
y_train = [0] * len(uw_comments[:5]) + [1] * len(uoft_comments[:5])





# Vectorize the comments
vectorizer = CountVectorizer()
vectorizer.fit(corpus)
x_train = vectorizer.transform(corpus)

# Train the model
classifier = MultinomialNB()
classifier.fit(x_train, y_train)

#get testing data
test_uw_comments = uw_submissions[3].comments.list()[:5]
test_uoft_comments = uoft_submissions[3].comments.list()[:5]
# take from another thread


test_corpus = [comment.body for comment in [test_uw_comments[0], test_uoft_comments[0]]]
y_test = [0, 1]
x_test = vectorizer.transform(test_corpus)


#Prediction
print(classifier.predict(x_test))
#actual
print(y_test)



