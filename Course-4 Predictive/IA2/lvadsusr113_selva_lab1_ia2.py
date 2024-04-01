# -*- coding: utf-8 -*-
"""LVADSUSR113-selva-Lab1-IA2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qYWfILOK0Jet1TpEIuU_a8ZPwaJfCTBq
"""

import pandas as pd

df_wine = pd.read_csv('/content/winequality-red.csv')
df_wine.info()

df_wine.head(2)

df_wine.isnull().sum()

df_wine = df_wine.bfill(axis='columns')
df_wine.isnull().sum()

import matplotlib.pyplot as plt
import seaborn as sns
plt.boxplot(df_wine['fixed acidity'])

df_wine = df_wine[df_wine['fixed acidity']<12.5]
df_wine = df_wine[df_wine['fixed acidity']>4]

plt.boxplot(df_wine['alcohol'])

df_wine = df_wine[df_wine['alcohol']<13.3]

plt.boxplot(df_wine['volatile acidity'])

df_wine = df_wine[df_wine['volatile acidity']<1.0]

plt.boxplot(df_wine['citric acid'])

df_wine = df_wine[df_wine['citric acid']<=0.8]

plt.boxplot(df_wine['residual sugar'])

df_wine = df_wine[df_wine['residual sugar']<4]

plt.boxplot(df_wine['chlorides'])

df_wine = df_wine[df_wine['chlorides']<0.11]
df_wine = df_wine[df_wine['chlorides']>0.04]

df_wine.loc[df_wine['quality'] <= 6, 'quality'] = 0
df_wine.loc[df_wine['quality'] > 6, 'quality'] = 1

sns.distplot(df_wine['fixed acidity'])

sns.distplot(df_wine['free sulfur dioxide'])

sns.distplot(df_wine['alcohol'])

sns.distplot(df_wine['density'])

#There is no categorical features

df_wine.duplicated().count()
df_wine.drop_duplicates()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(df_wine.drop('quality',axis='columns'),df_wine['quality'],test_size=0.3)

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100, random_state=42)

clf.fit(x_train, y_train)
predictions = clf.predict(x_test)

from sklearn.metrics import accuracy_score, precision_score, recall_score

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", round(accuracy*100,2),"%")
prec = precision_score(y_test, predictions)
print("Precision:", round(prec*100,2),"%")
recall = recall_score(y_test, predictions)
print("Recall:", round(recall*100,2),"%")