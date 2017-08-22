#Open API 공공데이터 

import requests
import urllib.parse as p
from urllib.request import Request,urlopen

import re

import csv

from datetime import date
import time

import pandas as pd
import os

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

SERVICE='LocalGovPriceInfoService'
OPERATION='getLocalGovPriceResearchSearch'
KEY='LNGx2DbXvy%2F1L3chL9isCcJR8kp0ja6pkn9049cAk1%2BmkfIP0SuKVS0bactIekU1utszRbKDtRpXPH88CARaXw%3D%3D'
numOfRows='10000'
pageNo='1'
_returnType='xml,json'
EXAMIN_AREA_CD='1102'

url='http://apis.data.go.kr/B552895/'
decode_key = p.unquote(KEY)
decode_return = p.unquote(_returnType)

#조사 일 
examin=re.compile('<examin_de>(.+?)</examin_de>')
#조사 지역명
examin_area_nm=re.compile('<examin_area_nm>(.+?)</examin_area_nm>')
#조사 지역코드
examin_area_cd=re.compile('<examin_area_cd>(.+?)</examin_area_cd>')
#조사 시장명
examin_mrkt_nm=re.compile('<examin_mrkt_nm>(.+?)</examin_mrkt_nm>')
#조사 시장코드
examin_mrkt_cd=re.compile('<examin_mrkt_cd>(.+?)</examin_mrkt_cd>')
#품목 명
prdlst_nm=re.compile('<prdlst_nm>(.+?)</prdlst_nm>')
#품목 코드
prdlst_cd=re.compile('<prdlst_cd>(.+?)</prdlst_cd>')
#품목 상세명
prdlst_detail_nm=re.compile('<prdlst_detail_nm>(.+?)</prdlst_detail_nm>')
#유통단계 구분
distb_step_se=re.compile('<distb_step_se>(.+?)</distb_step_se>')
#유통단계
distb_step=re.compile('<distb_step>(.+?)</distb_step>')
#등급
grad=re.compile('<grad>(.+?)</grad>')
#등급코드
grad_cd=re.compile('<grad_cd>(.+?)</grad_cd>')
#규격
stndrd=re.compile('<stndrd>(.+?)</stndrd>')
#조사가격
examin_amt=re.compile('<examin_amt>(.+?)</examin_amt>')


dayTuple = getTimeTuple('20140102', '20170821', 'D')

for d in dayTuple:
    examin_de = time.strftime('%Y%m%d',d)
    queryParams = SERVICE + '/' + OPERATION + '?'+ p.urlencode({ p.quote_plus('ServiceKey') : decode_key, p.quote_plus('numOfRows') : numOfRows , p.quote_plus('pageNo') : pageNo, p.quote_plus('_returnType') : decode_return, p.quote_plus('examin_de') : examin_de,p.quote_plus('examin_area_cd') : EXAMIN_AREA_CD })
    requestURL =url+queryParams
    print(requestURL)
    data = requests.get(requestURL).text
    examin_de_d = examin.findall(data)
    examin_area_nm_d = examin_area_nm.findall(data)
    examin_area_cd_d = examin_area_cd.findall(data)
    #examin_mrkt_nm_d = examin_mrkt_nm.findall(data)
    examin_mrkt_cd_d = examin_mrkt_cd.findall(data)
    prdlst_nm_d = prdlst_nm.findall(data)
    prdlst_cd_d = prdlst_cd.findall(data)
    prdlst_detail_nm_d = prdlst_detail_nm.findall(data)
    distb_step_se_d = distb_step_se.findall(data)
    distb_step_d = distb_step.findall(data)
    grad_d = grad.findall(data)
    grad_cd_d = grad_cd.findall(data)
    stndrd_d = stndrd.findall(data)
    examin_amt_d =  examin_amt.findall(data)
    
    d = {'examin_de_d':examin_de_d,'examin_area_nm_d':examin_area_nm_d,'examin_area_cd_d':examin_area_cd_d,'examin_mrkt_cd_d':examin_mrkt_cd_d,\
         'prdlst_nm_d':prdlst_nm_d,'prdlst_cd_d':prdlst_cd_d,'prdlst_detail_nm_d':prdlst_detail_nm_d,'distb_step_se_d':distb_step_se_d,\
         'distb_step_d':distb_step_d,'grad_d':grad_d,'grad_cd_d':grad_cd_d,'stndrd_d':stndrd_d,'examin_amt_d':examin_amt_d}
    df = pd.DataFrame(data=d)
    if not os.path.isfile('D:\yall.csv'):
        df.to_csv('D:\yall.csv',header=True)
    else:
        df.to_csv('D:\yall.csv', mode='a',header=False)