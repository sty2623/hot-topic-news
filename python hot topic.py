from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'C:\Users\tae young Shin\AppData\Local\Programs\Python\Python38-32\chromedriver_win32\chromedriver.exe')

driver.get('https://www.naver.com/')
time.sleep(3)                       #켜지는 시간 대기

text = driver.page_source

soup = BeautifulSoup(text, 'html.parser')

#l = []
f = open('output.txt', 'w')
for li in soup.select('#NM_RTK_ROLLING_WRAP > ul > li')[:20]:
    rank = li.a.span.text                   #검색어 순위
    keyword = li.a.select('span')[1].text   #검색어
#    print(rank, keyword)
    print(rank, keyword, file=f)            #텍스트 파일에 기록
#    l.append([rank, keyword])

f.close()

f = open('output.txt', 'r')

lines = f.readlines()
for line in lines:
    line = line.strip()                     #공백 제거
    print(line)                             #보낼때는 프린트가 아닌 다른것으로 변경
    
f.close()

driver.quit()
