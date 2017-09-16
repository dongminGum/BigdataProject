# -*- coding: utf-8 -*-

from pandas import DataFrame
import pandas as pd
import numpy as np
import csv
from datetime import date
from datetime import datetime
import datetime as dt
import time


before1= open("tempmerge3.csv")
before1_ = pd.read_csv(before1)
before1_ = before1_.drop(before1_.columns[0],axis=1)
before1_ = before1_.drop(before1_.columns[10],axis=1)
before1_ = before1_.drop(before1_.columns[10],axis=1)
before1_ = before1_.drop(before1_.columns[10],axis=1)

before1_.columns
before1_

#before2 = open("production.csv")
before2_ = pd.read_csv("production.csv")
before3 = open("weatherAll.csv")
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
dayTuple = getTimeTuple('20170101', '20170821','D')
weather2017_4 = DataFrame(0, index=np.arange(len(dayTuple)*len(dic)),columns=('date','temperature','groundSurface','dewPoint','rainfull','snow','newestSnow','windSpeed','pressure','humidity','cloud','solarRadiation','sunshine'))

#t시금치~, 양파~,
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
            for l in range(1,len(list(weather2017_4))):
                weather2017_4.loc[t][l] = weather2017_4.loc[t][l] + w_df_[list(weather2017_4)[l]].mul(w3,axis=0).sum()
        print(list(dic.keys())[j])
        weather2017_4.loc[t]=weather2017_4.loc[t]/len(period)            
        weather2017_4.loc[t].date = d
        print(i)
        
weather2017_4.to_csv("weather2017_4.csv")

#품목명 채우기        
w2014 = open('weather2014.csv')
w2014_ = pd.read_csv(w2014)
w2015 = open('weather2015.csv')
w2015_ = pd.read_csv(w2015)
w2016 = open('weather2016.csv')
w2016_ = pd.read_csv(w2016)
w2017 = open('weather2017.csv')
w2017_ = pd.read_csv(w2017)
len(w2014_['date'])


dic={'고구마':17,'감자':13,'무':10,'당근':11,'감귤':25,'수박':15,'딸기':15,'오이':20,'호박':12,'사과':16,'배추':13,'시금치':8,'상추':4,'양배추':12,'풋고추':6,'양파':20,'마늘':24}

dayTuple = getTimeTuple('20140101', '20141231','D')
for j in range(len(dic)):
    for i in range(len(dayTuple)):
        t=i+j*len(dayTuple)
        w2014_.loc[t,'product'] = list(dic.keys())[j]
        
dayTuple = getTimeTuple('20150101', '20151231','D')
for j in range(len(dic)):
    for i in range(len(dayTuple)):
        t=i+j*len(dayTuple)
        w2015_.loc[t,'product'] = list(dic.keys())[j]
        
dayTuple = getTimeTuple('20160101', '20161231','D')
for j in range(len(dic)):
    for i in range(len(dayTuple)):
        t=i+j*len(dayTuple)
        w2016_.loc[t,'product'] = list(dic.keys())[j]

dayTuple = getTimeTuple('20170101', '20170821','D')
for j in range(len(dic)):
    for i in range(len(dayTuple)):
        t=i+j*len(dayTuple)
        w2017_.loc[t,'product'] = list(dic.keys())[j]
        
w2014_
w2015_
w2016_
w2017_

weather_f = pd.concat([w2014_,w2015_,w2016_,w2017_])
weather_f.to_csv("weather_f.csv")
