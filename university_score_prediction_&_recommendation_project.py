# -*- coding: utf-8 -*-
"""University_Score_Prediction_&_Recommendation_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/131saF2HFQBhM-4C0fcCuFkc122Xxivka

## **University Score Prediction and Recommendation based on NIRF (Ministry of Education)**

**Objective**
1. Trying to predict the score of universities based on certain parameters set by NIRF which are
* Teaching Learning & Resources - These parameters are related to the core activities of any place of learning.
* Research and Professional Practice - Excellence in teaching and learning is closely associated with the scholarship.
* Graduation Outcome - This parameter forms the ultimate test of the effectiveness of the core teaching/learning.
* Outreach & Inclusivity - The Ranking framework lays special emphasis on representation of women.
* Perception - The ranking methodology gives a significant importance to the perception of the institution.

2. University recommendation based on the scores obtained by the universities.

**Introduction**

In this project, the application gathers and prepares the universities data from the NIRF website(of the desired year). Then feed the prepared data to the model so that it can learn. After then, feed the fresh data (University data) into the trained model and see if the model just trained predict it accurately or not. This application also recommend the university based on the the overall score and the scores under various parameters obtained by the universities.

**Python** is an open source programming language that was made to be easy-to-read and powerful. A Dutch programmer named Guido van Rossum made Python in 1991. He named it after the television show Monty Python's Flying Circus. Many Python examples and tutorials include jokes from the show.
Python is an interpreted language. Interpreted languages do not need to be compiled to run. A program called an interpreter runs Python code on almost any kind of computer. This means that a programmer can change the code and quickly see the results. This also means Python is slower than a compiled language like C, because it is not running machine code directly.

Python is a good programming language for beginners. It is a high-level language, which means a programmer can focus on what to do instead of how to do it. Writing programs in Python takes less time than in some other languages.
Python drew inspiration from other programming languages like C, C++, Java, Perl, and Lisp.

Python has a very easy-to-read syntax. Some of Python's syntax comes from C, because that is the language that Python was written in. But Python uses whitespace to delimit code: spaces or tabs are used to organize code into groups. This is different from C. In C, there is a semicolon at the end of each line and curly braces ({}) are used to group code. Using whitespace to delimit code makes Python a very easy-to-read language.

**Web Scraping**
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

html_content = requests.get('https://www.nirfindia.org/2022/UniversityRanking.html').text

uni_data = BeautifulSoup(html_content,'lxml')
uni_data

table = uni_data.find('table')
table

rows = table.find_all('tr')
rows

content = list()
for row in rows:
  cells = row.find_all(['td','th'])
  # print(cells)
  cells_text = [cell.text for cell in cells]
  content.append(cells_text)

df = pd.DataFrame(content)
df.to_csv('NIRF_UNiversity2022.csv')

"""### **Training, Prediction and Recommendation**

**Training Data**
Our training data consists of the totals obtained by Universities under various parameters (TLR, RPC,	GO, OI, PERCEPTION and Score). All training data can be retrieved from the file NIRF_University2022.csv.

**Prepare Training Data**
Model accepts the scores obtained by universities under the parameters as a input and labels so that for each evaluation the model knows which class the university belongs to and the overall score of the university (originally evaluated by NIRF).

**For example:** 

*(For Score Prediction)*

Features                                           

* TLR(100)	- 82.08
* RPC(100)  - 87.45
* GO(100)	  - 84.80
* OI(100)	  - 57.46
* PERCEPTION(100)	 - 100.00

Labels

* Score	- 83.57	

*(For Recommendation)*

Features                                           

* TLR(100)	- 82.08
* RPC(100)  - 87.45
* GO(100)	  - 84.80
* OI(100)	  - 57.46
* PERCEPTION(100)	 - 100.00
* Score	- 83.57

Labels

* Recommend - 1
"""

import pandas as pd

"""**Data Preparation**"""

df = pd.read_csv('/content/NIRF_UNiversity2022.csv')
df.head(5)

data = df.dropna()
data.head()

name=data['Name']
name

university_names = list()
for i in name:
  university_names.append(i.split('More')[0])
  # print(university_names)
university_names

# data['Name'] = pd.Series(university_names)
data = data.drop(['Name'],axis='columns')

data['Name'] = university_names

data

"""**Quick Vizualization**"""

import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_figwidth(8)
fig.set_figheight(6)
plt.plot(data['Score'],data['Rank'])
plt.xlabel('Score')
plt.ylabel('Rank')

data[['Score','Rank']].plot(figsize=(8,6))

"""**Linear** **Regression**

To predict the ranks based on the scores obtained by the universities(under NIRF annual rankings).
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df_train, df_test = train_test_split(data,test_size=0.2)

df_train.head()

df_test.head()

fig = plt.figure()
fig.set_figwidth(8)
fig.set_figheight(6)
plt.xlabel('Score')
plt.ylabel('Rank')
plt.scatter(df_train['Score'].values,df_train['Rank'].values,color='red')

mod = LinearRegression()
mod.fit(df_train[['Score']].values,df_train.Rank.values)

predicted_val = mod.predict(df_test[['Score']].values)

df_test['Rank']

predicted_val[predicted_val < 1] = 1
predicted_val

predicted_val = predicted_val.round(decimals=0, out=None)
predicted_val

mod.score(df_test[['Score']].values,df_test.Rank.values)

plt.scatter(df_test[['Score']].values,df_test.Rank.values, color='red')
plt.scatter(df_test[['Score']].values,predicted_val, color='green')
plt.xlabel('Score')
plt.ylabel('Rank')

"""**Multivariable Linear Regression**

To determine the University's overall Score based on examining the parameters TLR, RPC, GO, OI and Perception.
"""

model = LinearRegression()
model.fit(df_train[['TLR (100)', 'RPC (100)', 'GO (100)', 'OI (100)', 'PERCEPTION (100)']].values,df_train.Score.values)

y_predicted = model.predict(df_test[['TLR (100)', 'RPC (100)', 'GO (100)', 'OI (100)','PERCEPTION (100)']].values)

model.predict(df_test[['TLR (100)', 'RPC (100)', 'GO (100)', 'OI (100)','PERCEPTION (100)']].values)

model.score(df_test[['TLR (100)', 'RPC (100)', 'GO (100)', 'OI (100)','PERCEPTION (100)']].values,df_test.Score.values)

"""**Logistic Regression**

To recommend the University based on the Overall Score of Universities.

*Assumption*

Universities with overall Score greater than 45 are considered for recommendation and remaining with overall Score less than 45 are not considered for recommendation.
"""

recommend=[]
for row in data['Score']:
    if row <=45 :
        recommend.append('0')
    else: 
        recommend.append('1')

data['Recommend'] = recommend

data.head()

X_train, X_test, y_train, y_test = train_test_split(data[['Score']],data.Recommend,test_size=0.2)

fig = plt.figure()
fig.set_figwidth(15)
fig.set_figheight(5)
plt.scatter(X_train, y_train, marker = '+', color='red' )

from sklearn.linear_model import LogisticRegression

Log_reg = LogisticRegression()
Log_reg.fit(X_train,y_train)

y_predicted=Log_reg.predict(X_test)

Log_reg.score(X_test,y_predicted)

"""**Decision Tree Classifier**

To recommend the University evaluating the various attributes (evaluating the parameters) in our dataframe.
"""

data

input_data = data.drop(['Institute ID', 'City',	'State', 'Rank', 'Name', 'Recommend'], axis = 'columns')

input_data.head()

target = data['Recommend']

X_train, X_test, y_train, y_test = train_test_split(input_data, target, test_size = 0.2)

X_train.head()

from sklearn import tree

decision_model = tree.DecisionTreeClassifier()
decision_model.fit(X_train, y_train)

y_predicted = decision_model.predict(X_test)

y_predicted

decision_model.score(X_test,y_test)

plt.figure(figsize=(8,6))
tree.plot_tree(decision_model)

from sklearn.metrics import confusion_matrix
import seaborn as sn

cm = confusion_matrix(y_test, y_predicted)
cm

plt.figure(figsize=(8,6))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

"""**Software Requirements**

Languages and Packages used


●	Python3.6+ , Libraries - pandas, sklearn, bs4, matplotlib

●	Platform - Google Colab

Hardware Requirements

●	System Processor: i3  or later.

●	RAM: 4GB DDR RAM.(Minimum)

**Bibliography**

1. https://www.nirfindia.org/2022/UniversityRanking.html
"""