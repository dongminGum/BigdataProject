import pydoop.hdfs as hdfs
import pandas as pd
import csv

price1= hdfs.open("/data/y2014-1.csv",'r') 
df1 = pd.read_csv(price1)
price2=hdfs.open("/data/yall.csv",'r')
df2 = pd.read_csv(price2,error_bad_lines=False)

df3=df1.append(df2)
df3

price_index=hdfs.open("/data/price_index.csv",'r')
df4=pd.read_csv(price_index)
price_index=df4.transpose() 
price=price_index.rename(columns=price_index.iloc[1])
price.set_index([0:45]) ##point re index and delete 0,1 row

exchangerate=hdfs.open("/data/ExchangeRate.csv",'r')
df5=pd.read_csv(exchangerate)

merged = df3.merge(df5,left_on='examin_de_d',right_on='date',how='left')
merged.to_csv('/root/tempmerge.csv')
##### 
production1=hdfs.open("/data/production1.csv",'r')
df6=pd.read_csv(production1)

production2=hdfs.open("/data/production2.csv",'r')
df7=pd.read_csv(production2)

production3=hdfs.open("/data/production3.csv",'r')
df8=pd.read_csv(production3)

df9=df6.append(df7).append(df8)
df9
######

income=hdfs.open("/data/income.csv",'r')
df10=pd.read_csv(income)
df10


