from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'C:\Users\tae young Shin\AppData\Local\Programs\Python\Python38-32\chromedriver_win32\chromedriver.exe')

driver.get('https://www.naver.com/')
time.sleep(3)

text = driver.page_source

soup = BeautifulSoup(text, 'html.parser')

l = []
f = open('output.txt', 'w')
for li in soup.select('#NM_RTK_ROLLING_WRAP > ul > li')[:20]:
    rank = li.a.span.text
    keyword = li.a.select('span')[1].text
    print(rank, keyword)
    print(rank, keyword, file=f)
    l.append([rank, keyword])

f.close()

f = open('output.txt', 'r')

lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)


#while True:
#    line = f.readline()
#    if not line: break
#    print(line)
    
f.close()

driver.quit()
