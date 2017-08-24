import csv
from datetime import datetime
import time

files = ["weather-1.csv","weather-2.csv","weather-3.csv","weather-4.csv"]
new_file = open("weather2.csv","w",encoding='utf-8',newline='') #기상기후 데이터 정리 파일
writer = csv.writer(new_file)

#['지점번호', '지점', '일자', '평균기온 (℃)', '평균지면온도 (℃)', '평균이슬점온도 (℃)', 
#'일강수량 (mm)', '최심적설 (cm)', '최심신적설 (cm)', '평균풍속 (m/s)', 
#'평균현지기압 (hPa)', '평균습도 (%)', '평균전운량 (1/10)', '일사합 (MJ/m²)', '일조합 (hr)' ]
#헤더추가
writer.writerow(["id","city","date","temperature","groundSurface","dewPoint","rainfull","snow","newestSnow","windSpeed","pressure","humidity","cloud","solarRadiation","sunshine"])

for i in range(len(files)):
    _file = open(files[i], "r" ,encoding='utf-8')
    reader = csv.reader(_file)
    next(reader,None) #헤더제거
    _new = open("weather2.csv","a",encoding='utf-8',newline='')
    add = csv.writer(_new)
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        add.writerow([row[0],row[1],date.strftime('%Y%m%d'),row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[11],row[12],row[13],row[14],row[15]])
    
    _file.close()
    
new_file.close()