# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:33:23 2020

@author: james
"""

from selenium import webdriver
import time

driver = webdriver.Chrome('c:\\qa\\chromedriver.exe')

#티스토리 이동
driver.get('https://www.tistory.com/')

#로그인
driver.find_element_by_link_text('로그인하기').click() #로그인으로 이동
time.sleep(1)
driver.find_element_by_id("loginId").send_keys("[계정 입력]") #계정 입력
time.sleep(1)
driver.find_element_by_id("loginPw").send_keys("[비밀번호 입력]") #비밀번호 입력
time.sleep(1)
driver.find_element_by_xpath("//*[@id='authForm']/fieldset/button").click() #로그인 버튼 클릭
time.sleep(1)

#글쓰기 페이지까지 이동
driver.find_element_by_xpath("//*[@id='kakaoHead']/div/div[3]/div/a[2]/img").click() #계정정보 클릭
time.sleep(1)
driver.find_element_by_xpath("//*[@id='kakaoHead']/div/div[3]/div/div/div/div[2]/div/div[1]/a[1]").click() #첫번째 블로그 클릭
time.sleep(1)
driver.find_element_by_link_text('관리자').click() #관리자 페이지 클릭 
time.sleep(1)
driver.find_element_by_link_text('글쓰기').click() #글쓰기 버튼 클릭
time.sleep(1)

#글쓰기 진행
driver.find_element_by_xpath("//*[@id='editorContainer']/div[2]/textarea").send_keys("[제목 입력]") #제목작성
time.sleep(1)

#내용 입력은 아직 하지 못하였음.

driver.find_element_by_id("tagText").send_keys("[태그 입력]") #테그 작성
time.sleep(1)
driver.find_element_by_xpath("//*[@id='kakaoWrap']/div[3]/div[2]/button").click() #1차 등록버튼
time.sleep(1)
driver.find_element_by_xpath("//*[@id='editor-root']/div[6]/div/div/div/form/fieldset/div[3]/div/button[2]").click() #2차등록버튼 완료!

#종료
driver.close()