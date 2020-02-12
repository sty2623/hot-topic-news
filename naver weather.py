from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(r'C:\Users\tae young Shin\AppData\Local\Programs\Python\Python38-32\chromedriver_win32\chromedriver.exe', options=options)

driver.get('https://www.naver.com/')
time.sleep(3)                       #켜지는 시간 대기

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
time.sleep(3)

user_id = "sty2623@gmail.com"
user_pwd = "hottopic123"

elem = driver.find_element_by_xpath('//*[@id="id_email_2"]')
elem.send_keys(user_id)
elem = driver.find_element_by_xpath('//*[@id="id_password_3"]')
elem.send_keys(user_pwd)
elem.send_keys(Keys.RETURN)
    #elem = driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button')
    #elem.click()
time.sleep(2)

elem = driver.find_element_by_xpath('//*[@id="mArticle"]/div[3]/div/div[2]/table/tbody/tr/td[5]/button')
elem.click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[-1])
elem = driver.find_element_by_xpath('//*[@id="kakaoGnb"]/div/div/ul[2]/li[1]/a/span[1]')
elem.click()
time.sleep(1)
elem = driver.find_element_by_xpath('//*[@id="mArticle"]/div[2]/div[3]/div/div/li/a/div')
elem.click()

driver.switch_to.window(driver.window_handles[-1])
elem = driver.find_element_by_xpath('//*[@id="chatWrite"]')

elem = driver.find_element_by_xpath('//*[@id="kakaoWrap"]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[1]/input')
elem.send_keys(r'C:\Users\tae young Shin\Desktop\python\weather.png')
time.sleep(1)

driver.quit()



