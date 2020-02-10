from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'C:\Users\tae young Shin\AppData\Local\Programs\Python\Python38-32\chromedriver_win32\chromedriver.exe')

driver.get('https://news.naver.com/')
time.sleep(3) #웹 페이지 로드를 보장하기 위해 3초 쉬기

#

text = driver.page_source
#print(text)

soup = BeautifulSoup(text, 'html.parser')

#l = []
f = open('output2.txt', 'w')
for li in soup.select('#today_main_news > div.hdline_news > ul > li'):
    title = li.a.text.strip()
    url = 'http://news.naver.com' + li.a['href']
    print(title, url, file=f)
#    l.append([title, url])

f.close()

f = open('output2.txt', 'r')

lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)

f.close()

driver.quit()
