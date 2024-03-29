# -*- coding: utf-8 -*-
"""LVADSUSR113-Selva-Lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EAWAH0k1ZwoOKvjHTpfN4AWM-IFtQ9qC
"""

import pandas as pd

ex_data = pd.read_csv("/content/expenses.csv")

ex_data.info()

ex_data.describe()

nulls = ex_data.isnull().sum()
print(nulls)

# Outliers
import seaborn as sns
bmi_outliers = sns.boxplot(ex_data['bmi'])

age_outliers = sns.boxplot(ex_data['age'])

children_outliers = sns.boxplot(ex_data['children'])

charges_outliers = sns.boxplot(ex_data['charges'])
print(ex_data[ex_data['charges']>40000].count())

#Removing Outliers
def remove_outliers(A, threshold):
  return ex_data[A<threshold]

ex_data = remove_outliers(ex_data['charges'],40000)
ex_data = remove_outliers(ex_data['bmi'],45)
ex_data.count()

ex_data.info()

# Encoding the categorical features
from sklearn.preprocessing import LabelEncoder

lbl_enc = LabelEncoder()
ex_data['sex'] = lbl_enc.fit_transform(ex_data['sex'])
ex_data['smoker'] = lbl_enc.fit_transform(ex_data['smoker'])
ex_data['region'] = lbl_enc.fit_transform(ex_data['region'])

ex_data.head()

#Data cleaning and Feature selection
duplicates = ex_data.duplicated(keep=False)
ex_data['dup_bool'] = duplicates
ex_data[ex_data['dup_bool'] == True].count()

ex_data = ex_data[ex_data['dup_bool'] == False]
ex_data = ex_data.drop('dup_bool',axis=1)

sns.pairplot(ex_data)

# By the Above plots, It can be seen that Age, number of children and region has strong impact on the Insurance costs

from sklearn.model_selection import train_test_split

X = ex_data.drop('charges',axis=1)
y = ex_data['charges']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=30)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

trained_model = regressor.fit(X_train,y_train)

y_pred = trained_model.predict(X_test)

#Evaluation
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

mse = mean_squared_error(y_test,y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test,y_pred)

print('MSE: ',mse)
print('RMSE: ',rmse)
print('R-Squared: ',r2)