from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
# from bs4 import BeautifulSoup
# from urllib.request import urlopen

driver = webdriver.Chrome('C:/chromedriver.exe')
url = 'https://www.tistory.com/'
driver.get(url)
time.sleep(1)


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


login('eunsk31@daum.net', '')


def posting():
    driver.find_element_by_css_selector('.thumb_profile').click()
    driver.find_element_by_link_text('쓰기').click()
    driver.find_element_by_css_selector('.textarea_tit').send_keys("제목을 입력합니다.")
    # iframe : html 안에 또 다른 html이 있는 것
    # iframe 위치 지정. (iframe을 감싸고 있는 div 하위에 iframe이 있음)
    iframe = driver.find_element_by_css_selector('.mce-edit-area.mce-container.mce-panel.mce-stack-layout-item.mce-last iframe')
    # iframe으로 이동
    driver.switch_to.frame(iframe)
    # iframe 안의 콘텐츠 작성 영역(p 태그)에 내용 입력
    driver.find_element_by_tag_name('p').send_keys("내용을 입력합니다.")
    # 기존 프레임으로 이동
    driver.switch_to.default_content()
    driver.find_element_by_name('tagText').send_keys("태그1" + Keys.ENTER + "태그2" + Keys.ENTER + "태그3" + Keys.ENTER)
    driver.find_element_by_css_selector('.btn.btn-default').click()
    driver.implicitly_wait(5)

    if driver.find_element_by_id('open0').is_selected():
        print("비공개")
    elif driver.find_element_by_id('open15').is_selected():
        print("공개(보호)")
    else:
        print("공개")

    print(driver.find_element_by_id('open20').get_attribute('value'))
    print(driver.find_element_by_id('open15').get_attribute('value'))
    print(driver.find_element_by_css_selector('.btn.btn-default').is_enabled())

    delay = 5 # seconds

    while 1:
        try:
            WebDriverWait(driver, delay).until(expected_conditions.invisibility_of_element(
                (By.CSS_SELECTOR, '.tit_cont')
                )
            )
            driver.find_element_by_css_selector('.btn.btn-default').click()
            print("계속 클릭 중")
        except NoSuchElementException:
            print("클릭 그마안")
            break


posting()