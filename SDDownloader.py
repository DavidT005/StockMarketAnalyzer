#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing libraries
import pandas as pd #Manipulates databases
import datetime as dt #Creates time and date formats
import pandas_datareader.data as pdr #Tool for downloading data

'''
REFERENCES:
Ahmad Bazzi: https://www.youtube.com/watch?v=57qAxRV577c
'''


# In[14]:


def get_stock(symbol,y0,y1,d0 = 1, m0 = 1, d1 = 31, m1 = 12, source = "yahoo", save_data = True):
    '''
    Downloads stock data from the web given the stock symbol, the first and the last year of the study.
    The days and months for the initial and final dates can be changed, so can the source for the data.
    Set save_data as False and the function will return the stock data as a pandas dataframe.
    '''
    initial_date = dt.datetime(y0,m0,d0)
    final_date = dt.datetime(y1,m1,d1)
    stock_data = pdr.DataReader(symbol,source,initial_date,final_date)
    if (save_data == True):
        stock_data.to_csv(symbol + "-" + str(y0) + "-" + str(y1) + ".csv")
        return
    else:
        return stock_data

