import sys    
import os     

import pandas as pd    
import numpy as np     

from bs4 import BeautifulSoup    
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys

import time                      
import math

import pandas as pd

import csv 

from difflib import SequenceMatcher

path_driver = "chromedriver.exe"

driver = webdriver.Chrome(path_driver)

ad_list = [['경기 이천시 아리역로 37','경기 이천시 아리역로38번길 10-18']]
time_list = []

for ad1_name, ad2_name in ad_list:

    driver.get("https://map.kakao.com/")

    time.sleep(3)


    ad1 = driver.find_element_by_xpath('//*[@id="search.keyword.query"]')
    ad1.send_keys(ad1_name + Keys.ENTER)
    time.sleep(2)

    try:
        get_out = driver.find_element_by_xpath('/html/body/div[10]').click()
        get_out2 = driver.find_element_by_xpath('/html/body/div[10]/div').click()

        time.sleep(1)
    except:
        pass

    bt = driver.find_element_by_xpath('//*[@id="view.mapContainer"]/div[2]/div/div[6]/div[7]/div/div[2]/div[3]/div/div[2]/button')
    bt.click()

    time.sleep(1)


    start_p = driver.find_element_by_xpath("//button[.='" + '출발' + "']")
    start_p.click()

    time.sleep(1)

    get_out3 = driver.find_element_by_xpath('/html/body/div[10]/div/div').click()
    time.sleep(1)


    try:
        muji = driver.find_element_by_xpath('//*[@id="info.route.searchBox.list"]/div[2]').click()
    except:
        pass

    ad2 = driver.find_element_by_xpath('//*[@id="info.route.waypointSuggest.input1"]')

    ad2.send_keys(ad2_name + Keys.ENTER)

    time.sleep(2)


    car_bt = driver.find_element_by_xpath('//*[@id="cartab"]')
    car_bt.click()

    time.sleep(2)

    take_time = driver.find_element_by_xpath('//*[@id="info.flagsearch"]/div[6]/ul/li/div[1]/div/div[1]/p/span[1]')
    text = take_time.text

    time_list.append(text)


print(time_list)


driver.close()
