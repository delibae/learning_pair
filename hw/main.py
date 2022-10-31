# 각각 작성한 코드를 모두 합친 것입니다.
# 이름 밑에 자신이 작성한 코드를 넣었습니다.
# 한번에 돌아가기 위해 원본에서 일부 주석처리하고 수정한 부분 있습니다.
# 자세한 코드는 아래에 깃허브 링크 남깁니다.
# https://github.com/delibae/learning_pair

####송수민

from audioop import adpcm2lin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup

from webdriver_manager.chrome import ChromeDriverManager

import time
# import pyautogui
# import pyperclip

import pandas as pd
import re

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# service = Service('/Users/songsumin/Documents/chromedriver')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5)  # 웹페이지가 로딩 될때까지 5초는 기다림
driver.maximize_window()

ad_list = []
ad_list2 = []
ad_index = []

# 엑셀 불러오기
df = pd.read_excel("Book2.xlsx", sheet_name="주소 리스트")
for row in range(2, 15):  # 1714
    ad = df.iloc[row, 1]
    ad_list.append(ad)

for ad_name in ad_list:
    driver.get("https://map.kakao.com/")
    try:
        c1 = driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div/span')
        c1.click()
        raise Exception('No element to click')
    except Exception as e:
        print(e)

    # 검색
    ad1 = driver.find_element(By.XPATH, '//*[@id="search.keyword.query"]')
    ad1.click()
    ad1.send_keys(f'경기 이천시 {ad_name}' + Keys.ENTER)
    time.sleep(2)

    # 결과 가져오기
    try:
        ad2 = driver.find_element(By.XPATH, '//*[@id="info.search.place.list"]/li[1]/div[5]/div[2]/p[1]')
        text = ad2.text

        # 결과 리스트로 만들기
        ad_list2.append(text)
        raise Exception('No results found')
    except Exception as e:
        print(e)

driver.quit()

# 결과 엑셀로 옮기기
for i in range(len(ad_list2)):
    ad_index.append(f'{i}')

# excel_data1 = {'도로명': ad_list2}
# print(excel_data1)

# df1 = pd.DataFrame(excel_data1, index=ad_index, columns=['도로명'])
# excel_writer = pd.ExcelWriter('/Users/songsumin/Dev/tutorial/learning_pair/addressList/Book3.xlsx', engine='openpyxl')
# df1.to_excel(excel_writer, index=True, sheet_name='도로명 리스트')
# excel_writer.save()


###배한진

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
# ad_list = create_ad_list('Book3.xlsx')
ad_list = ad_list2
print(ad_list)

# key:주소1인덱스_주소2인덱스, value: 주소1 <-> 주소2 소요시간
time_dict = {}

# 겹치는 작업 없도록 반복문 생성
for i in range(len(ad_list)):
    for j in range(i + 1, len(ad_list)):

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
            get_out = driver.find_element(By.XPATH, '/html/body/div[10]').click()
            get_out2 = driver.find_element(By.XPATH, '/html/body/div[10]/div').click()

            time.sleep(1)
        except:
            pass

        # 길찾기 버튼 클릭
        try:
            bt = driver.find_element(By.CLASS_NAME, 'btn_direction')
            bt.click()
            time.sleep(1)
        except:
            print("error: btn_direction click error")

        # 출발 버튼 클릭
        try:
            start_p = driver.find_element(By.XPATH, "//button[.='" + '출발' + "']")
            start_p.click()
            time.sleep(1)
        except:
            print("error: start button click error")

        # 팝업창 제거
        try:
            get_out3 = driver.find_element(By.XPATH, '/html/body/div[10]/div/div').click()
            time.sleep(1)
        except:
            pass

        # 두번째 주소 클릭 전 input 활성화
        try:
            muji = driver.find_element(By.XPATH, '//*[@id="info.route.searchBox.list"]/div[2]').click()
        except:
            pass

        # 두번째 주소 입력
        try:
            ad2 = driver.find_element(By.XPATH, '//*[@id="info.route.waypointSuggest.input1"]')
            ad2.send_keys(ad2_name + Keys.ENTER)
        except:
            print("error: second address input error")

        time.sleep(2)

        # 차량탭으로 이동
        try:
            car_bt = driver.find_element(By.XPATH, '//*[@id="cartab"]')
            car_bt.click()
        except:
            print("error: car tab switch error")

        time.sleep(1)

        # 소요시간 추출
        try:
            take_time = driver.find_element(By.XPATH,
                                            '//*[@id="info.flagsearch"]/div[6]/ul/li/div[1]/div/div[1]/p/span[1]')
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
# with open('time_dict.pickle', 'wb') as fw:
#     pickle.dump(time_dict, fw)

### 김명섭


# 전체 주소:일련번호
import queue
from tabnanny import check
from tracemalloc import start

from numpy import Inf


address_dict = {'Loc1':1,'Loc2':2,'Loc3':3,'Loc4':4,'Loc5':5}
# 전체주소-전체주소: 소요시간
# time_dict = {'1-2':30,'1-3':40,'1-4':10,'1-5':90,'2-3':60,'2-4':80,'2-5':25,'3-4':5,'3-5':15,'4-5':45}
time_dict = time_dict

enterType = False
# false 일 때가 화면 터치, true 일때가 엑셀 파일

# 파일 입력 부분은 최종 보고서시 작성

# 입력 받은 리스트 (현재는 테스트 값)
addressList = ['Loc1','Loc2','Loc5']
serialNumList = [] # 일련번호 리스트

# 일련번호 리스트 채우기
for i in range(len(addressList)):
    if addressList[i] in address_dict:
        serialNumList.insert(i,address_dict[addressList[i]])

class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)]for _ in range(size)]
    def add(self, i , j):
        if i == j:
            routeGraph.graph[i][j] = 999
        else:
            time = time_dict[str(serialNumList[i]) + "-" + str(serialNumList[j])]
            routeGraph.graph[j][i] = time
            routeGraph.graph[i][j] = time

# 일련번호 리스트 이용해서 그래프 만들기
routeGraph = Graph(len(serialNumList))

for i in range (len(serialNumList)):
    for j in range (i, len(serialNumList)):
        routeGraph.add(i,j)


# 경로 생성

checkPoint = "Loc5"
checkPointNum = address_dict[checkPoint]
nextNum = 0


shortRoute = 999 # 최단 경로를 999로 리셋

visited = [checkPointNum] # 방문한 장소

# 큐형식으로 작업 공간 생성
current = []
originCurrent =[]
def creating_queue (pointNum): # 경로에 대한 시간을 담은 큐 작성
    global current
    global originCurrent
    current = [] # 경로 찾는 큐 리셋
    originCurrent = [] # 경로 찾는 큐 리셋
    for i in serialNumList: # 체크 포인트에서 가능한 경로 큐에 추가
        current.append(routeGraph.graph[serialNumList.index(pointNum)][serialNumList.index(i)])
        originCurrent.append(routeGraph.graph[serialNumList.index(pointNum)][serialNumList.index(i)])
    for j in visited: # 방문한 장소는 current 리스트에서 제거
        print("방문 :", j)
        current.remove(routeGraph.graph[serialNumList.index(pointNum)][serialNumList.index(j)])
        print("커런트 : ",current)




# 알고리즘 사용
for i in range(len(serialNumList)-1):
    #print(i)
    creating_queue(checkPointNum) # 큐 생성
    for i in current:
        if shortRoute > i: # 현재가지고 있는 최단 거리보다 작으면 최단거리 다시 저장
            shortRoute = i
    print("오리진 : ",originCurrent)
    visited.append(serialNumList[originCurrent.index(shortRoute)]) # 방문 리스트에 저장
    checkPointNum = serialNumList[originCurrent.index(shortRoute)] # 체크 포인트 방문한 곳으로 저장
    shortRoute=999 # 최단 거리 리셋

    print(visited)


# 변경 사항: 경로 설정 완료
# 최종 보고서때 까지 작업 해야하는 사항: 엑셀 파일 가져오기, 화면 출력


