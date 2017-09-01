
from bs4 import BeautifulSoup
import urllib.request    


  
weather = ['폭염', '장마', '우박','가뭄','폭염','병해충','폭설','태풍','폭우','고온다습','집중호우','호우','무더위','이상기온']
def get_text(URL):
    
        source_code_from_URL = urllib.request.urlopen(URL)
        soup = BeautifulSoup(source_code_from_URL,'lxml',from_encoding='utf-8')
        text = ''
        
    #    for item in soup.find_all('li', { "class" : "txt_inline" }):
    #    URL = 'https://search.naver.com/search.naver?ie=utf8&where=news&query=%EA%B3%84%EB%9E%80%20%ED%8F%AD%EB%9D%BD&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:dd,p:all,a:all&mynews=0&start=1%&refresh_start=0'
            
    #    for item in soup.find_all('li', id = 'sp_nws41'):
    #        text = text + item.find_all(text=True)[2]
            
        for item in soup.find_all('ul', {'class':'type01'}):
            
            for litag in item.find_all('li'):
                
    #            for ddtag in litag.find_all('dd', {'class':'txt_inline'}):
    #            text = text + str(litag.find_all(text=True))
    #            print(type(str(litag.find_all(text=True)).split(',')))
                count=0
                for i in range(len(weather)):
                    if str(litag.find_all(text=True)).find(weather[i]) == -1:
                        count = count + 1
                if count == len(weather):
                    for ddtag in litag.find_all('dd', {'class':'txt_inline'}):
                        text = text + ddtag.find_all(text=True)[2]
    
     #           text = text + litag.find_all('dd', {'class':'txt_inline'})[]
    
    
        return text
    
def main():
       
        #product=['egg','strawberry','cabbage','onion','garlic','green','rice','chicken','sweet','potato','scabbage','spinach','lettuce','watermelon','cucumber','pumpkin','daikon','greenchilli','apple','orange']
        product=['%EA%B3%84%EB%9E%80','%EB%94%B8%EA%B8%B0','%EB%B0%B0%EC%B6%94','%EC%96%91%ED%8C%8C','%EB%A7%88%EB%8A%98','%ED%8C%8C','%EC%8C%80','%EB%8B%AD%EA%B3%A0%EA%B8%B0','%EA%B3%A0%EA%B5%AC%EB%A7%88','%EA%B0%90%EC%9E%90','%EC%96%91%EB%B0%B0%EC%B6%94','%EC%8B%9C%EA%B8%88%EC%B9%98','%EC%83%81%EC%B6%94','%EC%88%98%EB%B0%95','%EC%98%A4%EC%9D%B4','%ED%98%B8%EB%B0%95','%EB%AC%B4','%ED%92%8B%EA%B3%A0%EC%B6%94','%EC%82%AC%EA%B3%BC','%EA%B0%90%EA%B7%A4']
        #product=[]
        for m in range(len(product)):
            OUTPUT_FILE_NAME=product[m]+'Up.txt'
            open_output_file = open('C:/Users/admin/Desktop/productUp/'+OUTPUT_FILE_NAME,'w',encoding='utf8')
            i = 1
            while i < 4000:
               URL = 'https://search.naver.com/search.naver?ie=utf8&where=news&query='+product[m]+'%20%ED%8F%AD%EB%93%B1&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:dd,p:all,a:all&mynews=0&start=%idx%&refresh_start=0'
               print(product[m])
               result_text = get_text(URL.replace('%idx%', str(i)))
               open_output_file.write(result_text)
               i = i + 10
        open_output_file.close()
        
if __name__ == '__main__':
        main()