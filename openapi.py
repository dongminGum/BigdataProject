import requests
import urllib.parse as p
from urllib.request import Request,urlopen
from DateRange import *
import time

dayTuple = getTimeTuple('2015-12-08', '2017-08-22', 'D')
for d in dayTuple:
    import urllib.parse as p
    import re
    import csv
    import pandas as pd
    SERVICE='StatsInfoService'
    OPERATION='getvRealtimeMktStatsInfo'
    KEY='nN%2Bi%2BQZlHA3bPle7s8qIiXcNE7gcTgzEqRW46PwT2q%2BBlsj9glkgRC81GkQDYXKZni%2FvhGfHJ4cfc%2FZTLGUxFA%3D%3D'

    numOfRows='10000'
    pageNo='1'
    whsal_code='110001'
    _returnType='xml'
    delng_de=time.strftime('%Y%m%d',d)
    
    url='http://apis.data.go.kr/B552895/'
    decode_key = p.unquote(KEY)
    queryParams = SERVICE + '/' + OPERATION + '?'+ p.urlencode({ p.quote_plus('ServiceKey') : decode_key, p.quote_plus('numOfRows') : numOfRows , p.quote_plus('pageNo') : pageNo, p.quote_plus('whsal_code') : whsal_code, p.quote_plus('_returnType') : _returnType, p.quote_plus('delng_de') : delng_de})
    
    a =url + queryParams
    print(a)
    data=requests.get(a).text
    
    delng_de=re.compile('<delng_de>(.+?)</delng_de>') ## 거래 일자
    whsal_code=re.compile('<whsal_code>(.+?)</whsal_code>') ## 시장 코드    
    whsal_nm=re.compile('<whsal_nm>(.+?)</whsal_nm>') ## 시장 코드    
    mlsfc_code=re.compile('<mlsfc_code>(.+?)</mlsfc_code>') ## 품목코드
    mlsfc_nm=re.compile('<mlsfc_nm>(.+?)</mlsfc_nm>') ## 품목이름-중분류
    std_prdlst_code=re.compile('<std_prdlst_code>(.+?)</std_prdlst_code>') ## 품목코드
    std_prdlst_nm=re.compile('<std_prdlst_nm>(.+?)</std_prdlst_nm>') ##품목이름-소분류
    std_unit_code=re.compile('<std_unit_code>(.+?)</std_unit_code>') ## 단위 코드
    std_unit_nm=re.compile('<std_unit_nm>(.+?)</std_unit_nm>') ## 단위 이름
    std_grad_code=re.compile('<std_grad_code>(.+?)</std_grad_code>') ## 등급 코드
    std_grad_nm=re.compile('<std_grad_nm>(.+?)</std_grad_nm>') ## 등급 이름
    delng_prut_code=re.compile('<delng_prut_code>(.+?)</delng_prut_code>') ## 거래 단량
    delng_qy=re.compile('<delng_qy>(.+?)</delng_qy>') ## 거래 수량 = 유통량
    
    delng_de_d=delng_de.findall(data)
    whsal_code_d=whsal_code.findall(data)
    whsal_nm_d=whsal_nm.findall(data)
    mlsfc_code_d=mlsfc_code.findall(data)
    mlsfc_nm_d=mlsfc_nm.findall(data)
    std_prdlst_code_d=std_prdlst_code.findall(data)
    std_prdlst_nm_d=std_prdlst_nm.findall(data)
    std_unit_code_d=std_unit_code.findall(data)
    std_unit_nm_d=std_unit_nm.findall(data)
    std_grad_code_d=std_grad_code.findall(data)
    std_grad_nm_d=std_grad_nm.findall(data)
    delng_prut_code_d=delng_prut_code.findall(data)
    delng_qy_d=delng_qy.findall(data)
    
    dic = {'delng_de':delng_de_d,'whsal_code':whsal_code_d,'whsal_nm':whsal_nm_d,'mlsfc_code':mlsfc_code_d,'mlsfc_nm':mlsfc_nm_d,
         'std_prdlst_code':std_prdlst_code_d,'std_prdlst_nm':std_prdlst_nm_d,'std_unit_code':std_unit_code_d,'std_unit_nm':std_unit_nm_d,
         'std_grad_code':std_grad_code_d,'std_grad_nm':std_grad_nm_d,'delng_prut_code':delng_prut_code_d,'delng_qy':delng_qy_d}
    df = pd.DataFrame(data=dic)
    df.to_csv('D:\datasample\Report1.csv',mode='a',header=False)
    """
    with open('D:\Report.csv', "w") as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        for i in range(len(delng_de_d)):
            writer.writerow([delng_de_d[i],whsal_code_d[i],whsal_nm_d[i],mlsfc_code_d[i],mlsfc_nm_d[i],std_prdlst_code_d[i],std_prdlst_nm_d[i],std_unit_code_d[i],std_unit_nm_d[i],std_grad_code_d[i],std_grad_nm_d[i],delng_prut_code_d[i],delng_qy_d[i]])
    """"