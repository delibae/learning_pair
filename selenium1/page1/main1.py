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


path_driver = "./chromedriver"

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


ad_list = ['경기 이천시 아리역로 37','경기 이천시 아리역로38번길 10-18','경기 이천시 부발읍 경충대로 1918-18','경기 이천시 설성면 설가로 219','경기 이천시 장호원읍 대서리 산 63-1']
time_dict = {}

for i in range(len(ad_list)):
    for j in range(i+1, len(ad_list)):

        ad1_name = ad_list[i]
        ad2_name = ad_list[j]

        print(ad1_name,ad2_name)

        driver.get("https://map.kakao.com/")

        time.sleep(3)
        try:
            ad1 = driver.find_element(By.XPATH, '//*[@id="search.keyword.query"]')
            ad1.send_keys(ad1_name + Keys.ENTER)
            time.sleep(2)
        except:
            print("error: first address input error")


        try:
            get_out = driver.find_element(By.XPATH,'/html/body/div[10]').click()
            get_out2 = driver.find_element(By.XPATH,'/html/body/div[10]/div').click()

            time.sleep(1)
        except:
            pass

        bt = driver.find_element(By.CLASS_NAME,'btn_direction')
        bt.click()


        time.sleep(1)


        start_p = driver.find_element(By.XPATH,"//button[.='" + '출발' + "']")
        start_p.click()

        time.sleep(1)

        try:
            get_out3 = driver.find_element(By.XPATH,'/html/body/div[10]/div/div').click()
            time.sleep(1)
        except:
            pass


        try:
            muji = driver.find_element(By.XPATH,'//*[@id="info.route.searchBox.list"]/div[2]').click()
        except:
            pass

        try:
            ad2 = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
            ad2.send_keys(ad2_name + Keys.ENTER)
        except:
            print("error: second address input error")

        time.sleep(2)

        try:
            car_bt = driver.find_element(By.XPATH,'//*[@id="cartab"]')
            car_bt.click()
        except:
            print("error: car tab switch error")

        time.sleep(1)

        try:
            take_time = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[6]/ul/li/div[1]/div/div[1]/p/span[1]')
            text = take_time.text
        except:
            print("error: no time value")

        time_dict[f'{i}_{j}'] = text

print(time_dict)

driver.close()

with open('time_dict.pickle','wb') as fw:
    pickle.dump(time_dict, fw)


