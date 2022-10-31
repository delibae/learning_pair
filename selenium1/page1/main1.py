import sys    
import os     

import pandas as pd    
import numpy as np     

from bs4 import BeautifulSoup    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time                      
import math

import csv

import pickle

# 주소 리스트 엑셀에서 불러오는 함수
def create_ad_list(path):
    ex = pd.read_excel(path)
    ad_list = ex['도로명'].to_list()
    return ad_list



# 시간 텍스트를 정수형으로 변환하는 함수


def to_int(text):
    hour = text.find('시')

    minute = text.find('분')

    if hour == -1:
        text = int(text[:minute])
    else:
        text = text.split('시간')
        if minute != -1:
            text2 = text[1].split('분')
            text = int(text[0]) * 60 + int(text2[0])
        else:
            text = int(text[0]) * 60

    print(text)
    return text

# 크롬 드라이버 생성
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 주소 리스트 불러오기
ad_list = create_ad_list('Book3.xlsx')
print(ad_list)

# key:주소1인덱스_주소2인덱스, value: 주소1 <-> 주소2 소요시간
time_dict = {}

# 겹치는 작업 없도록 반복문 생성
for i in range(len(ad_list)):
    for j in range(i+1, len(ad_list)):

        # 주소1 주소2 불러오기
        ad1_name = ad_list[i]
        ad2_name = ad_list[j]

        # print(ad1_name,ad2_name)

        # 카카오맵 열기
        driver.get("https://map.kakao.com/")

        time.sleep(3)

        # 첫번째 주소 입력
        try:
            ad1 = driver.find_element(By.XPATH, '//*[@id="search.keyword.query"]')
            ad1.send_keys(ad1_name + Keys.ENTER)
            time.sleep(2)
        except:
            print("error: first address input error")

        # 팝업창 제거
        try:
            get_out = driver.find_element(By.XPATH,'/html/body/div[10]').click()
            get_out2 = driver.find_element(By.XPATH,'/html/body/div[10]/div').click()

            time.sleep(1)
        except:
            pass

        # 길찾기 버튼 클릭
        try:
            bt = driver.find_element(By.CLASS_NAME,'btn_direction')
            bt.click()
            time.sleep(1)
        except:
            print("error: btn_direction click error")



        # 출발 버튼 클릭
        try:
            start_p = driver.find_element(By.XPATH,"//button[.='" + '출발' + "']")
            start_p.click()
            time.sleep(1)
        except:
            print("error: start button click error")

        # 팝업창 제거
        try:
            get_out3 = driver.find_element(By.XPATH,'/html/body/div[10]/div/div').click()
            time.sleep(1)
        except:
            pass

        # 두번째 주소 클릭 전 input 활성화
        try:
            muji = driver.find_element(By.XPATH,'//*[@id="info.route.searchBox.list"]/div[2]').click()
        except:
            pass
        
        # 두번째 주소 입력
        try:
            ad2 = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
            ad2.send_keys(ad2_name + Keys.ENTER)
        except:
            print("error: second address input error")

        time.sleep(2)

        # 차량탭으로 이동
        try:
            car_bt = driver.find_element(By.XPATH,'//*[@id="cartab"]')
            car_bt.click()
        except:
            print("error: car tab switch error")

        time.sleep(1)

        # 소요시간 추출
        try:
            take_time = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[6]/ul/li/div[1]/div/div[1]/p/span[1]')
            text = take_time.text
        except:
            print("error: no time value")

        # text에 있는 시간 값을 분 단위의 정수형으로 변환
        text = to_int(text)
        # time_dict에 소요시간 추가
        time_dict[f'{i}-{j}'] = text


# time_dict 출력
print(time_dict)

# 드라이버 종료
driver.quit()

# time_dict data를 pickle 형태로 저장
with open('time_dict.pickle', 'wb') as fw:
    pickle.dump(time_dict, fw)

#완료?

