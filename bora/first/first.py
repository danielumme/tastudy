from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen

driver = webdriver.Chrome('C:/chromedriver.exe')
url = 'https://www.tistory.com/'
driver.get(url)
time.sleep(3)


# 네이버는 로그인 자동입력방지 시스템 때문에 drop
# def login(id, pw):
#     driver.find_element_by_css_selector('.ico_local_login.lang_ko').click()
#     driver.find_element_by_name('id').send_keys(id)
#     driver.find_element_by_name('pw').send_keys(pw)
#     driver.find_element_by_name('pw').send_keys(Keys.ENTER)


def login(id, pw):
    driver.find_element_by_link_text('로그인하기').click()
    driver.find_element_by_name('loginId').send_keys(id)
    driver.find_element_by_name('password').send_keys(pw)
    driver.find_element_by_name('password').send_keys(Keys.ENTER)


login(input("ID: "), input("PW: "))


def posting():
    driver.find_element_by_css_selector(".thumb_profile").click()
    driver.find_element_by_link_text('쓰기').click()
    driver.find_element_by_css_selector(".textarea_tit").send_keys("제목 입력")
    driver.find_element_by_css_selector("#tinymce").send_keys("내용 입력")
    driver.find_element_by_name('tagText').send_keys("태그1" + Keys.ENTER)


posting()