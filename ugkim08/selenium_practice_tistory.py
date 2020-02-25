from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = ('C:/chromedriver.exe')
driver = webdriver.Chrome(path)
url = 'https://www.tistory.com/'

time.sleep(1)

# 티스토리 접속
driver.get(url)

# 브라우저 크기를 1260 x 890으로 조정
driver.set_window_size(1280, 950)

time.sleep(1)

# 티스토리 메인 > 로그인 페이지 이동
driver.find_element(By.XPATH, '//*[@id="kakaoHead"]/div/div[3]/div/a[1]').click()

# email주소 및 pw입력
driver.find_element(By.NAME, 'loginId').send_keys('Email')
time.sleep(0.5)
driver.find_element(By.NAME, 'password').send_keys('PW')
time.sleep(0.5)

# 로그인 버튼 클릭
driver.find_element(By.CLASS_NAME, 'btn_login').click()
time.sleep(1)

# 썸네일 아이콘을 통해 글쓰기 페이지 진입
driver.find_element(By.CLASS_NAME, 'thumb_profile').click()
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="kakaoHead"]/div/div[3]/div/div/div/div[2]/div/div/a[2]').click()


time.sleep(2)

driver.close()
