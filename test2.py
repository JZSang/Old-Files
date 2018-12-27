from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

corpus = ["STRING", "STRING", "BADSTRING"] ## Put email messages here
y = ['spam', 'spam', 'not-spam']      ## Tag emails as spam/not-spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

classifier = MultinomialNB()
classifier.fit(X, y)

print(classifier.predict([["string"], X])) ## Use the machine learning model here!