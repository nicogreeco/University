import pandas as pd
#'pandas' allow us to manage data, work on data and do some statistic,
#  goes hand by hand with an other
# import 'numpy' that is used for calcules and usally iported together
import numpy as np


## 1 dimentional data type -- .Series
# similiar to list but different work of index
lst = [1,2,3,4]
s = pd.Series(lst)
print (s[2])
# we can change index instead of classic list 0,1,2,3...
myindex = ['s1', 's2', 's3', 's4']
swi = pd.Series(lst, index= myindex)
print(swi['s1'])

randoms = pd.Series(np.random.randn(4), index=myindex)
# Creating a new Series with index of myindex that has as
# element random numbers called with np.random

data = {'s1': 12, 's2': 8, 's3': 4, 's4': 6}
sdict = pd.Series(data)
# Can also create a Series in one step using dictionary whose keys will became our indxù

sdict - swi
# will subtract to all element of sdict the element of swi with same index

df1 = pd.DataFrame({
    'swi' : swi,
    'sdict' : sdict,
    'random' : randoms
})
# This will create a table with the datas of the 3 Series (of course should have same index)


df1.describe()
# create tables with quartiles...

df1['newcolomn'] = 1
# Create a new colomn with 1 as value for each index
df1.sort_values(by='swi', inplace = True)
# Sorting the datafreame according on values of the colomn swi, the ',inplace = True, will suvrascrive 
# the same tab. Otherwise we can save it in a new tab
# all of this command on dataframe are not permanent, to make them so we use inplace = True in the ()

df1[0:2] # Access to the first two rows
df1['s1':'s3'] # Access by the index
df1[df1.sdict < 1] # Access to all row with sdict lower than 1
# We cna save them in a new dataframe to work on them separately

df1[['swi','sdict']] # Giving a list with colomn we can access to a dataframe with just selected colomn


np.nan #it is a NaN object
pd.isna(df1) # Wil scan the dataframe and return wich are NaN values
# other stuff to deal with NaN values


df1.mean(0) # mean on colomns (axis 0)
df1.mean(1) # mean on rows (axis 1)

df1.apply(lambda row: row['swi'] * 10, axis = 1) # Used to apply a soecific funcion.
# lambda row: --> for roe in list
# this is the fastest way to aply a funtion to our dataframe
