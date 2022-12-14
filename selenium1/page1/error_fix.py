import pickle

# a = ['0_29','30_59','60_99','100_129','130_159','160_189','190_219','220_249','250_last']
# path = './final_data/100_200/time_dict_'
# path_1 = './final_data/100_200/error_list_'
# time_dict = {}
# for i in a:
#     t_path = path + i + '.pickle'
#     with open(t_path,'rb') as f:
#         t = pickle.load(f)
#     time_dict.update(t)
#
# error_list_to = []
#
# for i in a:
#     e_path = path_1 + i + '.pickle'
#     with open(e_path,'rb') as f:
#         e = pickle.load(f)
#     error_list_to.extend(e)
#
# print(len(time_dict))
# print(len(error_list_to))


with open('fixed_data/time_dict1.pickle', 'rb') as f:
    time_dict = pickle.load(f)
with open('fixed_data/error_list1.pickle', 'rb') as f:
    error_list_to = pickle.load(f)

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

    return text


# 크롬 드라이버 생성
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 주소 리스트 불러오기
ad_list = create_ad_list('Book3.xlsx')
print(ad_list)


# key:주소1인덱스_주소2인덱스, value: 주소1 <-> 주소2 소요시간

error_list = []

# print(len([k for k, v in time_dict.items() if v == -1]))

###


for m in range(len(error_list_to)):

    i = ad_list.index(error_list_to[m][0])
    j = ad_list.index(error_list_to[m][1])
    print(time_dict[f'{i}-{j}'] == -1)
    # start = time.time()
    error = 0
    # 주소1 주소2 불러오기
    ad1_name = ad_list[i]
    print(ad_list[i])
    ad2_name = ad_list[j]
    print(ad_list[j])
    # print(ad1_name,ad2_name)

    # 카카오맵 열기
    driver.get("https://map.kakao.com/")

    time.sleep(2)

    # 첫번째 주소 입력
    try:
        ad1 = driver.find_element(By.XPATH, '//*[@id="search.keyword.query"]')
        ad1.send_keys(ad1_name + Keys.ENTER)
        time.sleep(1)
    except:
        error = 1
        print("error: first address input error")

    # 팝업창 제거
    try:
        get_out = driver.find_element(By.XPATH, '/html/body/div[10]').click()
        get_out2 = driver.find_element(By.XPATH, '/html/body/div[10]/div').click()

        # time.sleep(1)
    except:
        pass

    # 길찾기 버튼 클릭
    try:
        bt = driver.find_element(By.CLASS_NAME, 'btn_direction')
        bt.click()
        # time.sleep(1)
    except:
        error = 1
        print("error: btn_direction click error")

    # 출발 버튼 클릭
    try:
        start_p = driver.find_element(By.XPATH, "//button[.='" + '출발' + "']")
        start_p.click()
        # time.sleep(1)
    except:
        error = 1
        print("error: start button click error")

    # 팝업창 제거
    try:
        get_out3 = driver.find_element(By.XPATH, '/html/body/div[10]/div/div').click()
        # time.sleep(1)
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
        error = 1
        print("error: second address input error")

    time.sleep(1)

    # 차량탭으로 이동
    try:
        car_bt = driver.find_element(By.XPATH, '//*[@id="cartab"]')
        car_bt.click()
    except:
        error = 1
        print("error: car tab switch error")

    time.sleep(1)

    # 소요시간 추출
    try:
        take_time = driver.find_element(By.XPATH,
                                        '//*[@id="info.flagsearch"]/div[6]/ul/li/div[1]/div/div[1]/p/span[1]')
        text = take_time.text
    except:
        error = 1
        print("error: no time value")

    # text에 있는 시간 값을 분 단위의 정수형으로 변환
    if error == 0:
        try:
            text = to_int(text)
            # time_dict에 소요시간 추가
            time_dict[f'{i}-{j}'] = text
            print(error)
        except:
            error = 1
            print("error: to_int error")
            print(error)
    else:
        error = 1
        print(error)
        error_list.append([ad1_name, ad2_name])
        time_dict[f'{i}-{j}'] = -1

# time_dict 출력
print(len([k for k, v in time_dict.items() if v == -1]))
print(error_list)

# 드라이버 종료
driver.quit()

# time_dict data를 pickle 형태로 저장
with open('../../gui/make_pickle/time_dict.pickle', 'wb') as fw:
    pickle.dump(time_dict, fw)

with open('fixed_data/error_list.pickle', 'wb') as fw:
    pickle.dump(error_list, fw)

