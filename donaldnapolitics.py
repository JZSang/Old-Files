import praw

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import MultinomialNB

reddit = praw.Reddit(
    client_id = '2D96SxaOxD31IQ',
    client_secret = 'KyPYwaOWiMdfWXZauI1of_BmLu0',
    user_agent = 'what am i doing' # Name your user agent whatever you like
)

donaldsubmission = list(reddit.subreddit('the_donald').top(limit=10))

top_donald = donaldsubmission[1]

donaldcomments = top_donald.comments.list()


politicssubmission = list(reddit.subreddit('dota2').top(limit=10))

top_politics = politicssubmission[1]

politicscomments = top_politics.comments.list()



corpus = [comment.body for comment in (donaldcomments[:100] + politicscomments[:100])]

y_train = [0] * len(donaldcomments[:100]) + [1] * len(politicscomments[:100])


vectorizer = CountVectorizer()
vectorizer.fit(corpus)
x_train = vectorizer.transform(corpus)


classifier = MultinomialNB()
classifier.fit(x_train, y_train)

testdonald = donaldsubmission[2].comments.list()[:10]
testpolitics = politicssubmission[2].comments.list()[:10]
test_comments = testdonald + testpolitics

test_corpus = [comment.body for comment in test_comments]
y_test = [0] * len(testdonald) + [1] * len(testpolitics)
x_test = vectorizer.transform(test_corpus)

print(classifier.predict(x_test))

print(y_test)


