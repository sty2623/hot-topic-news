from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#driver = webdriver.Chrome(r'C:\Users\tae young Shin\AppData\Local\Programs\Python\Python38-32\chromedriver_win32\chromedriver.exe')

def macro():
    driver = webdriver.Chrome(r'C:\Users\tae young Shin\AppData\Local\Programs\Python\Python38-32\chromedriver_win32\chromedriver.exe')

    driver.get('https://www.naver.com/')
    time.sleep(10)                       #켜지는 시간 대기

    text = driver.page_source

    soup = BeautifulSoup(text, 'html.parser')

    f = open('output.txt', 'w')
    for li in soup.select('#NM_RTK_ROLLING_WRAP > ul > li')[:20]:
        rank = li.a.span.text                   #검색어 순위
        keyword = li.a.select('span')[1].text   #검색어
        print(rank, keyword, file=f)            #텍스트 파일에 기록

    f.close()

    driver.get('https://news.naver.com/')       #뉴스 사이트 이동
    time.sleep(10)                               #딜레이

    text = driver.page_source

    soup = BeautifulSoup(text, 'html.parser')

    f = open('output2.txt', 'w')
    for li in soup.select('#today_main_news > div.hdline_news > ul > li'):
        title = li.a.text.strip()
        url = 'http://news.naver.com' + li.a['href']
        print(title, url, file=f)

    f.close()

    #카카오톡 로그인
    driver.get('https://accounts.kakao.com/login/kakaoforbusiness?continue=https://center-pf.kakao.com/')
    time.sleep(8)

    user_id = "sty2623@gmail.com"
    user_pwd = "hottopic123"

    elem = driver.find_element_by_xpath('//*[@id="id_email_2"]')
    elem.send_keys(user_id)
    elem = driver.find_element_by_xpath('//*[@id="id_password_3"]')
    elem.send_keys(user_pwd)
    elem.send_keys(Keys.RETURN)
    #elem = driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button')
    #elem.click()
    time.sleep(5)

    elem = driver.find_element_by_xpath('//*[@id="mArticle"]/div[3]/div/div[2]/table/tbody/tr/td[5]/button')
    elem.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])
    elem = driver.find_element_by_xpath('//*[@id="kakaoGnb"]/div/div/ul[2]/li[1]/a/span[1]')
    elem.click()
    time.sleep(5)
    elem = driver.find_element_by_xpath('//*[@id="mArticle"]/div[2]/div[3]/div/div/li/a/div')
    elem.click()

    driver.switch_to.window(driver.window_handles[-1])
    elem = driver.find_element_by_xpath('//*[@id="chatWrite"]')

    action = webdriver.ActionChains(driver)     #마우스, 키보드 제어

    f = open('output.txt', 'r')

    lines = f.readlines()
    for line in lines:                         
        line = line.strip()
        elem.send_keys(line)
        action.key_down(Keys.SHIFT).perform()
        elem.send_keys(Keys.RETURN)
        action.key_up(Keys.SHIFT).perform()
        
    f.close()

    #elem = driver.find_element_by_xpath('//*[@id="kakaoWrap"]/div[1]/div[2]/div/div[2]/div[2]/form/fieldset/button')
    #elem.click()
    elem.send_keys(Keys.RETURN)
    time.sleep(1)

    f = open('output2.txt', 'r')

    lines = f.readlines()                       #뉴스기사 카톡으로 보내기
    for line in lines:
        line = line.strip()
        elem.send_keys(line)
        action.key_down(Keys.SHIFT).perform()
        elem.send_keys(Keys.RETURN)
        action.key_up(Keys.SHIFT).perform()

    f.close()

    elem.send_keys(Keys.RETURN)
    time.sleep(3)

    driver.quit()

def weather():
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(r'C:\Users\tae young Shin\AppData\Local\Programs\Python\Python38-32\chromedriver_win32\chromedriver.exe', options=options)

    driver.get('https://www.naver.com/')
    time.sleep(10)                       #켜지는 시간 대기

    elem = driver.find_element_by_xpath('//*[@id="query"]')
    elem.send_keys("광주 날씨")
    elem.send_keys(Keys.RETURN)

    driver.execute_script("window.scrollTo(0, 1080)") 
    elem = driver.find_element_by_class_name('weather_area._mainArea')
    #elem = driver.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]')
    elem_png = elem.screenshot_as_png
    with open("weather.png", "wb") as file:
        file.write(elem_png)

    driver.get('https://accounts.kakao.com/login/kakaoforbusiness?continue=https://center-pf.kakao.com/')
    time.sleep(8)

    user_id = "sty2623@gmail.com"
    user_pwd = "hottopic123"

    elem = driver.find_element_by_xpath('//*[@id="id_email_2"]')
    elem.send_keys(user_id)
    elem = driver.find_element_by_xpath('//*[@id="id_password_3"]')
    elem.send_keys(user_pwd)
    elem.send_keys(Keys.RETURN)
        #elem = driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button')
        #elem.click()
    time.sleep(8)

    elem = driver.find_element_by_xpath('//*[@id="mArticle"]/div[3]/div/div[2]/table/tbody/tr/td[5]/button')
    elem.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])
    elem = driver.find_element_by_xpath('//*[@id="kakaoGnb"]/div/div/ul[2]/li[1]/a/span[1]')
    elem.click()
    time.sleep(5)
    elem = driver.find_element_by_xpath('//*[@id="mArticle"]/div[2]/div[3]/div/div/li/a/div')
    elem.click()

    driver.switch_to.window(driver.window_handles[-1])
    elem = driver.find_element_by_xpath('//*[@id="chatWrite"]')

    elem = driver.find_element_by_xpath('//*[@id="kakaoWrap"]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[1]/input')
    elem.send_keys(r'C:\Users\tae young Shin\Desktop\python\weather.png')
    time.sleep(3)

    driver.quit()



tm = time.localtime()                       #현재시간 반환

while True:
    if tm.tm_hour == 7 and tm.tm_min <=29:
        try:
            print("날씨 시작")
            weather()
            time.sleep(60 * 30)
        except:
            print("비정상 종료")
            try:
                driver.quit()
            except:
                pass
            
    if 8 <= tm.tm_hour and (tm.tm_hour <= 20 and tm.tm_min <= 30):                #아침 8시부터 저녁 8시까지만 실
        try:
            print("매크로 시작")
            macro()
            time.sleep(60 * 120)
        except:
            print("비정상 종료")
            try:
                driver.quit()
            except:
                pass
