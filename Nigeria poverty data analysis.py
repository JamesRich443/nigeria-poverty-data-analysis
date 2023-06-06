#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import mysql.connector
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
import os

db=mysql.connector.connect(
host="localhost",
user="root",
passwd="cuddy123",
database="Global poverty and inequality dataset"
)
 
my_cursor=db.cursor()




df = pd.read_sql('''
select country  ,year, AVG(headcount_ratio_international_povline) as avg_pov from pip_dataset 
 where reporting_level='national' and country='nigeria'  group by country ,year

''',db)




X = df['year']
y = df['avg_pov']
cats=df['country']


x_arr = X.to_numpy().reshape(-1,1)
y_arr= y.to_numpy()




X_train ,X_test , y_train,y_test=train_test_split(x_arr ,y_arr ,test_size=0.3)
    
regr= LinearRegression()

regr.fit(X_train ,y_train)

r_sq = regr.score(x_arr, y_arr)


predicted_values= np.array([2025, 2026, 2027, 2028, 2029,]).reshape(-1,1)


pred = regr.predict(predicted_values)





plt.plot(predicted_values,pred)


print(pred)
print(r_sq)

if r_sq < 0.3:
    print("this is a weak score and this visualization should be taken with  a grain of salt")
elif r_sq > 0.7:
    print("this score is strong and the visualization is most likely accurate")
else:
    print("this is a moderate score and this visualization is fairly accurate")
    

 


# In[ ]:





# In[ ]:





# In[ ]:




