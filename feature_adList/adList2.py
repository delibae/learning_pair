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

service = Service('/Users/songsumin/Documents/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5) # 웹페이지가 로딩 될때까지 5초는 기다림
driver.maximize_window()

ad_list = []
ad_list2 = []
ad_index = []

# 엑셀 불러오기
df = pd.read_excel("/Users/songsumin/Dev/tutorial/learning_pair/addressList/Book2.xlsx", sheet_name = "주소 리스트")
for row in range(2, 15): #1714
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

driver.close()

# 결과 엑셀로 옮기기
for i in range(len(ad_list2)):
    ad_index.append(f'{i}')

excel_data1 = {'도로명' : ad_list2}
print(excel_data1)  

df1 = pd.DataFrame(excel_data1,index = ad_index, columns = ['도로명'])
excel_writer = pd.ExcelWriter('/Users/songsumin/Dev/tutorial/learning_pair/addressList/Book3.xlsx', engine='openpyxl')
df1.to_excel(excel_writer, index=True, sheet_name='도로명 리스트')
excel_writer.save()