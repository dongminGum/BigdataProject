# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 09:17:05 2017

@author: admin
"""
from pandas import Series,DataFrame
import pandas as pd
import os
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
    
    
for x in range(2015,2018,2):
    for y in range(1,13):
        if y<10:
            excel=str(x)+str(0)+str(y)
            print(excel)
            data = open("C:/Users/admin/Desktop/income/income"+excel+".xls","r",encoding="utf-8")
            
        else:
            excel=str(x)+str(y)
            print(excel)
            data = open("C:/Users/admin/Desktop/income/income"+excel+".xls","r",encoding="utf-8")
        
        
        html = data.read()
        parsed_html = BeautifulSoup(html)
        print (parsed_html.thead.text.split('\n')[4])

        list=[]
        pre_date=parsed_html.thead.text.split('\n')[4]
        date=parsed_html.thead.text.split('\n')[5]
        print(pre_date)
        print(date)

        parsed_html.tbody.text.split('\n')
        for z in parsed_html.tbody.text.split('\n'):
            if z.strip():
                list.append(z)
                
        print(list)
        newlist=[]
        newlist2=[]
        newlist3=[]

        for s in list:
            if '계' in s:
                a=list[list.index(s):list.index(s)+3]
                a.extend([pre_date])
                newlist.append(a)
                newlist2.append(list[list.index(s)])
                newlist2.append(list[list.index(s)+3])
                newlist2.append(list[list.index(s)+4])
                newlist2.append(date)
                newlist3.append(newlist2)
                newlist2=[]
        #201405 data
        print(newlist)
        #201505 data 
        print(newlist3)


        newlist=newlist+newlist3
        print(newlist)


        data=pd.DataFrame(newlist,columns=['AGCODE','WEIGHT','PRICE','YEAR'])
        label=['AGCODE','WEIGHT','PRICE','YEAR']
        frame=DataFrame(data,columns=label)
        frame
    
        if not os.path.isfile('C:\income\income.csv'):
            frame.to_csv('C:\income\income.csv',header=True)
        else:
            frame.to_csv('C:\income\income.csv',mode='a',header=False)



