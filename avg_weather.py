# -*- coding: utf-8 -*-

from pandas import DataFrame
import pandas as pd
import numpy as np
import csv
from datetime import date
from datetime import datetime
import datetime as dt
import time


before1= open("C:/Users/hg961/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/tempmerge3.csv")
before1_ = pd.read_csv(before1)
before1_ = before1_.drop(before1_.columns[0],axis=1)
before1_ = before1_.drop(before1_.columns[10],axis=1)
before1_ = before1_.drop(before1_.columns[10],axis=1)
before1_ = before1_.drop(before1_.columns[10],axis=1)

before1_.columns
before1_

before2 = open("C:/Users/hg961/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/production.csv")
before2_ = pd.read_csv(before2)
before3 = open("C:/Users/hg961/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/weatherAll.csv")
before3_ = pd.read_csv(before3)
before2_
before3_

def getTimeTuple(startTimeStr, endTimeStr, rangeType):
    #init vars
    startTime = ''
    endTime = ''
    startTimeDigit = 0
    endTimeDigit = 0
    addRange = 0

    timeList = []
    timeTuple = ()
     
    #set rangeTime
    if rangeType == 'H':
        addRange = 60 * 60
    elif rangeType == 'D':
        addRange = 60 * 60 * 24
    else:
        return ()

    #set startTime, endTime 
    startTime = time.strptime(startTimeStr, '%Y%m%d')
    startTimeDigit = time.mktime(startTime)
    endTime = time.strptime(endTimeStr, '%Y%m%d')
    endTimeDigit = time.mktime(endTime)

    if startTimeDigit >= endTimeDigit:
        timeList.append(time.localtime(startTimeDigit))
        return timeTuple

    #set time tuple
    while True:
        if startTimeDigit > endTimeDigit:
            break;
        timeList.append(time.localtime(startTimeDigit))
        #print localtime(startTimeDigit)
        startTimeDigit += addRange

    timeTuple = tuple(timeList)
    return timeTuple


    

dic={'고구마':17,'감자':13,'무':10,'당근':11,'감귤':25,'수박':15,'딸기':15,'오이':20,'호박':12,'사과':16,'배추':13,'시금치':8,'상추':4,'양배추':12,'풋고추':6,'양파':20,'마늘':24}
dayTuple = getTimeTuple('20160101', '20161231','D')
weather2016 = DataFrame(0, index=np.arange(len(dayTuple)*len(dic)),columns=('date','temperature','groundSurface','dewPoint','rainfull','snow','newestSnow','windSpeed','pressure','humidity','cloud','solarRadiation','sunshine'))


for j in range(len(dic)):
    for i in range(len(dayTuple)):
        t=i+j*365
        d = time.strftime('%Y%m%d',dayTuple[i])
        start = datetime.strptime(d,'%Y%m%d') - dt.timedelta(weeks=list(dic.values())[j])
        dateform_s = start.strftime('%Y%m%d')
        period = getTimeTuple(dateform_s,d,'D')
        for k in range(len(period)):
            dd = time.strftime('%Y%m%d',period[k])
            w_df = before3_[before3_['date'].astype(str) == dd]
            w = before2_[(before2_['product'] == list(dic.keys())[j]) & (before2_['year'].astype(str) == dd[:4])]
            w_df_=w_df.sort_values(by='city')
            w2=w.sort_values(by='city')
            w3=np.array(w2.weight)
            for l in range(1,len(list(weather2016))):
                weather2016.loc[t][l] = weather2016.loc[t][l] + w_df_[list(weather2016)[l]].mul(w3,axis=0).sum()
        print(list(dic.keys())[j])
        weather2016.loc[t]=weather2016.loc[t]/len(period)            
        weather2016.loc[t].date = d
        print(i)
        


weather2016.to_csv("C:/Users/hg961/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/weather2016.csv")