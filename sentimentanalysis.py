# -*- coding: utf-8 -*-
"""SentimentAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yr2tup38mcrC9gkJE6uoCQcX07ri40rE
"""

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import numpy as np

import nltk
nltk.download('stopwords')
import nltk
nltk.download('punkt')
import nltk
nltk.download('wordnet')

# Loading the dataset
data = pd.read_csv('sentiment_dataset.csv', header=None)

# Separating the text and target variables
X = data.iloc[:, 0].values
y = data.iloc[:, 1].values

X = list(filter(None,X))
y = list(filter(None,y))

# Preprocessing the text
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

for i in range(len(X)):
    text = X[i]
    # Tokenization
    X = data.iloc[:, 0].astype(str).values

    words = word_tokenize(text.lower())
    # Lemmatization and stop-word removal
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    X[i] = ' '.join(words)

X = pd.DataFrame(X)

# Creating features using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Predicting the sentiment of the test set
y_pred = clf.predict(X_test)

# Evaluating the performance of the model
print('Accuracy:', accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=['Negative', 'Neutral', 'Positive']))