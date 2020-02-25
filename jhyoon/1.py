from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# 같은 폴더에 크롬 드라이버 구동
# 헤드레스 처리
options = Options()
options.headless = True
드라이버 = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

티스토리 = 'https://www.tistory.com/'



id = input('id 입력 : ')
pw = input('pw 입력 : ')

# 로그인
def login(id, pw):
    드라이버.find_element_by_link_text('로그인하기').click()
    드라이버.find_element_by_name('loginId').send_keys(id)
    드라이버.find_element_by_name('password').send_keys(pw)
    드라이버.find_element_by_name('password').send_keys(Keys.ENTER)


# 티스토리 페이지 이동
드라이버.get(티스토리)

# login() 호출 입력받은 id, pw 변수 대입
login(id,pw)
