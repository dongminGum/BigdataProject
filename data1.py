import pandas as pd
import csv
# 가격 테이블 불러오기
price1= open("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/y2014-1.csv",'r') 
df1 = pd.read_csv(price1)
price2= open("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/yall.csv")
df2 = pd.read_csv(price2,error_bad_lines=False)

df3=df1.append(df2)
df3=df3.drop(df3.columns[0],axis=1)

# 환율 테이블 불러오기
exchangerate=open("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/ExchangeRate.csv",'r')
df4=pd.read_csv("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/ExchangeRate.csv")

# 가격 테이블과 환율 테이블을 합침
merged = df3.merge(df4,left_on='examin_de_d',right_on='date',how='left')
columns=['date','open','highprice','lowprice','change%'] # 필요없는 열 삭제
merged = merged.drop(columns,axis=1)
merged['yyyymm']=merged['examin_de_d']
for i in range(len(merged['examin_de_d'])):
    merged['yyyymm'][i] = str(merged['examin_de_d'][i])[:6]
merged

merged.to_csv('C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/tempmerge.csv')

"""
price_index=open("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/price_index.csv",'r')
"""
df5=pd.read_csv("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/price_index.csv")
price_index=df5.transpose() 
price=price_index.rename(columns=price_index.iloc[1])
price=price.drop(price.index[:2])
price=price.reset_index()
price['index']=price['index'].str.replace('. ','')
price

##### 
production1=open("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/production1.csv",'r')
df6=pd.read_csv("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/production1.csv",sep=',')

production2=open("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/production2.csv",'r')
df7=pd.read_csv("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/production2.csv",sep=',')

production3=open("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/production3.csv",'r')
df8=pd.read_csv("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/production3.csv",sep=',')

df9=df6.append(df7).append(df8)
df9

### 수입 유통량

df10=pd.read_csv("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/income.csv",sep=',')
df10=df10.drop(df10.columns[0],axis=1)
df10['YEAR']=df10['YEAR'].str.replace('년','').str.replace('월','')
df10
### 국내 유통량
df11=pd.read_csv("C:/Users/Jang Kihyuk/Desktop/Predicting_Argricultual_Product_Price-master/DataSet/circulationall.csv",sep=',')
df11
