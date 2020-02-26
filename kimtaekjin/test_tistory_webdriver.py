# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)  #메시지 'DeprecationWarning' 무시용 구문

driver = webdriver.Chrome('c:\\qa\\chromedriver.exe')
driver.get('https://www.tistory.com/')

###해당 정보는 따로 뺴서 불러올 수 있음 ###
did = "[계정을 입력하세요]" #계정
pw = "[비밀번호를 입력하세요]" #비번
title = "반갑습니다." #글제목
content = "환영합니다.\n반갑습니다\n고마워" #글내용
tag = "welcome!!" #태그


#로그인 리스트로 구성요소 작성[행동,xpath, 입력값 있으면 넣고, 없으면 쓰지 않음]
login = [
['로그인버튼 클릭', "//*[@id='kakaoHead']/div/div[3]/div/a[1]"],
['계정 입력', "//*[@id='loginId']", did],
['비밀번호 입력', "//*[@id='loginPw']", pw],
['로그인버튼 클릭', "//*[@id='authForm']/fieldset/button"],
['계정정보버튼 클릭', "//*[@id='kakaoHead']/div/div[3]/div/a[2]/img"],
['블로그버튼 클릭', "//*[@id='kakaoHead']/div/div[3]/div/div/div/div[2]/div/div[1]/a[1]"],
['관리자버튼 클릭', "//*[@id='footer']/p/a[2]"],
['글쓰기버튼 클릭', "//*[@id='mFeature']/div[2]/a[1]"]
]

#글작성 리스트로 구성요소 작성[행동,xpath, 입력값 있으면 넣고, 없으면 쓰지 않음]
write =[
['카테고리선택 클릭',"//*[@id='editorContainer']/div[1]/div/button/i[1]"],
['카테고리 드롭박스 선택 클릭',"//*[@id='editorContainer']/div[1]/div[2]/div/div[2]/span"],
['제목 입력',"//*[@id='editorContainer']/div[2]/textarea", title],
['태그 입력',"//*[@id='tagText']", tag],
['글내용 입력',"//*[@id='tinymce']", content],
['1차 저장버튼 클릭',"//*[@id='kakaoWrap']/div[3]/div[2]/button"],
['최종 저장버튼 클릭',"//*[@id='editor-root']/div[6]/div/div/div/form/fieldset/div[3]/div/button[2]"]
]

#driver.find_element_by_xpath 함수
def finder(x):
    try: 
        if len(x) == 2:
            driver.find_element_by_xpath(x[1]).click()
        elif len(x) == 3:
            if x[0] =='글내용 입력':
                driver.switch_to_frame(0)
                driver.find_element_by_xpath(x[1]).send_keys(x[2])                
                driver.switch_to.default_content()
            else:
                driver.find_element_by_xpath(x[1]).send_keys(x[2])        
        time.sleep(1)
        print(x[0] + "진행 완료!")
    
    except Exception as e:
        print("에러발생!")
        print(e)
        
#로그인
[finder(i) for i in login]

#글쓰기
[finder(i) for i in write]

#종료
driver.close()