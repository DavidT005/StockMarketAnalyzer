#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing libraries
import pandas as pd #To manipulate databases
import datetime as dt #To manipulate time and date formats
import pandas_datareader.data as pdr #Tool for downloading data

'''
MAIN REFERENCES
Ahmad Bazzi: https://www.youtube.com/watch?v=57qAxRV577c
'''


# In[14]:


def get_stock(symbol,y0,y1,d0 = 1, m0 = 1, d1 = 31, m1 = 12, source = "yahoo", save_data = True):
    initial_date = dt.datetime(y0,m0,d0)
    final_date = dt.datetime(y1,m1,d1)
    stock_data = pdr.DataReader(symbol,source,initial_date,final_date)
    if (save_data == True):
        stock_data.to_csv(symbol + "-" + str(y0) + "-" + str(y1) + ".csv")
        return
    else:
        return stock_data

