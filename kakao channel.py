from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'C:\Users\tae young Shin\AppData\Local\Programs\Python\Python38-32\chromedriver_win32\chromedriver.exe')

driver.get('https://accounts.kakao.com/login/kakaoforbusiness?continue=https://center-pf.kakao.com/')
time.sleep(3)

user_id = "sty2623@gmail.com"
user_pwd = "hottopic123"

elem = driver.find_element_by_xpath('//*[@id="id_email_2"]')
elem.send_keys(user_id)
elem = driver.find_element_by_xpath('//*[@id="id_password_3"]')
elem.send_keys(user_pwd)
elem.send_keys(Keys.RETURN)
time.sleep(2)


#driver.get('https://center-pf.kakao.com/_MIPCxb/messages/new/feed')
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
elem.send_keys("asdf")
elem.send_keys(Keys.RETURN)
time.sleep(1)

driver.close()
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
