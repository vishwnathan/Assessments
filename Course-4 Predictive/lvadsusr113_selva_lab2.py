# -*- coding: utf-8 -*-
"""LVADSUSR113-Selva-Lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PZqSiqlMFiwoBYgZPDtprwLxZ4QrZLXx
"""

import pandas as pd

book_data = pd.read_csv("/content/booking.csv")

book_data.info()

book_data.head()

book_data.describe()

nulls = book_data.isnull().sum()
print(nulls)

import seaborn as sns
avg_price_outliers = sns.boxplot(book_data['average price'])

book_data = book_data[book_data['average price']<200]

lead_time_outliers = sns.boxplot(book_data['lead time'])

book_data = book_data[book_data['lead time']<300]

book_data.info()

# Encoding
from sklearn.preprocessing import LabelEncoder

lbl_enc = LabelEncoder()
book_data['type of meal'] = lbl_enc.fit_transform(book_data['type of meal'])
book_data['room type'] = lbl_enc.fit_transform(book_data['room type'])
book_data['market segment type'] = lbl_enc.fit_transform(book_data['market segment type'])
book_data['booking status'] = lbl_enc.fit_transform(book_data['booking status'])

import matplotlib.pyplot as plt
plt.scatter(book_data['number of adults'],book_data['average price'])

plt.scatter(book_data['number of children'],book_data['average price'])



plt.scatter(book_data['number of weekend nights'],book_data['average price'])

plt.scatter(book_data['number of week nights'],book_data['average price'])

# Removing unnecessary columns (Feature selection)
book_data = book_data.drop(columns=['date of reservation','Booking_ID'],axis=1)

# Removing duplicates
duplicates = book_data.duplicated(keep=False)
book_data['dup_bool'] = duplicates
book_data[book_data['dup_bool'] == True].count()

book_data = book_data[book_data['dup_bool'] == False]
book_data = book_data.drop('dup_bool',axis=1)
book_data.count()

from sklearn.model_selection import train_test_split

X = book_data.drop('booking status',axis=1)
y = book_data['booking status']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=30)

from sklearn.linear_model import LogisticRegression

regressor = LogisticRegression(random_state=0,max_iter=10000)

trained_model = regressor.fit(X_train,y_train)

y_pred = trained_model.predict(X_test)

from sklearn.metrics import accuracy_score,precision_score, recall_score, f1_score

accuracy = accuracy_score(y_test,y_pred)
precision = precision_score(y_test,y_pred)
recall = recall_score(y_test,y_pred)

print('Accuracy score: ',round(accuracy*100,2),'%')
print('Precision score: ',round(precision*100,2),'%')
print('Recall score: ',round(recall*100,2))

