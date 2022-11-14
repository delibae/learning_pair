import eel
import pandas as pd
import json
from pandas import json_normalize
import route_module as rt
import time
import pickle

time_gap,time1 = rt.get_time_gap()


addressList = ['경기 이천시 부발읍 경충대로 1918-18' , '경기 이천시 신둔면 석동로 3', '경기 이천시 설성면 설가로 219', '경기 이천시 부발읍 경충대로1722번길 54', '경기 이천시 장호원읍 대서리 산 63-1']


# recent1 = ['Loc0', 'Loc1', 'Loc3', 'Loc4', 'Loc2']
# recent2 = ['Loc0', 'Loc1', 'Loc3', 'Loc4', 'Loc2']
# recent3 = ['Loc0', 'Loc1', 'Loc3', 'Loc4', 'Loc2']

### 제거 실험 필요
serialNumList = []

# address_dict = {'Loc0': 0, 'Loc1': 1, 'Loc2': 2, 'Loc3': 3, 'Loc4': 4}
# 전체주소-전체주소: 소요시간
# time_dict = {'0-1': 30, '0-2': 40, '0-3': 10, '0-4': 90, '1-2': 60, '1-3': 80, '1-4': 25, '2-3': 5, '2-4': 15,
#              '3-4': 45}

### 이 딕셔너리도 미리 pickle로 만들어 두면 됨
# convert_address_dict = {v: k for k, v in address_dict.items()}


with open('./data/recent1.pickle', 'rb') as f:
    recent1 = pickle.load(f)
print(recent1)
with open('./data/recent2.pickle', 'rb') as f:
    recent2 = pickle.load(f)
print(recent2)
with open('./data/recent3.pickle', 'rb') as f:
    recent3 = pickle.load(f)
print(recent3)
with open('./data/time_dict.pickle', 'rb') as f:
    time_dict = pickle.load(f)
print(time_dict)
with open('./data/address_dict.pickle', 'rb') as f:
    address_dict = pickle.load(f)
print(address_dict)
with open('./data/convert_address_dict.pickle', 'rb') as f:
    convert_address_dict = pickle.load(f)
print(convert_address_dict)

# Set web files folder
eel.init('web')

is_new = 0

@eel.expose  # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)


@eel.expose
def get_file(file):

    print(type(file))
    info = json.loads(file)
    df = json_normalize(info)
    global ad_list
    ad_list = df['도로명']
    global addressList
    addressList = ad_list.to_list()
    global is_new
    is_new = 1


    print(ad_list)

    ####ad1_list ad2_list ad3_list pickle 바꾸기


### ad_list => address_list 전환 필요
@eel.expose
def find_path():
    if is_new == 1:
        ## 최신 파일 교체
        with open('./data/recent2.pickle', 'wb') as f:
            pickle.dump(recent1, f, pickle.HIGHEST_PROTOCOL)
        with open('./data/recent3.pickle', 'wb') as f:
            pickle.dump(recent2, f, pickle.HIGHEST_PROTOCOL)
        with open('./data/recent1.pickle', 'wb') as f:
            pickle.dump(addressList, f, pickle.HIGHEST_PROTOCOL)


    routeGraph = rt.Graph(len(addressList), addressList, address_dict, time_dict)
    pivot = address_dict.get(addressList[0])
    ### n 값 결정 알고리즘 필요

    target_second = 2
    n = rt.find_n(len(addressList),target_second,time_gap,time1)
    print("len of addressList", len(addressList))
    print("calculated n: ",n)

    a = rt.frm(routeGraph, n, pivot,routeGraph.serialNumList)

    global path_time
    pivot, path, path_time = a.complete_path()

    global final_ad
    final_ad = rt.serial_to_ad(path,convert_address_dict)
    print(final_ad)

    eel.check()

    ### 나중에 지울것
    time.sleep(1)

    eel.next_page()



i = 1


@eel.expose
def on_load():
    global path_size
    global i
    global final_ad
    global path_time

    print("i", i)
    path_size = len(final_ad)

    current_ad = final_ad[i]
    rest_time = sum(path_time[:])
    eel.first_data(current_ad, str(rest_time))

@eel.expose
def b_load():
    global path_size
    global i
    global final_ad
    global path_time

    print("i", i)
    path_size = len(final_ad)

    current_ad = final_ad[i]
    rest_time = path_time[-1]
    eel.first_data(current_ad, str(rest_time))
@eel.expose
def next_path():
    global path_size
    global i
    global final_ad
    global path_time

    print("i", i)
    if i < path_size-1:
        i += 1
        current_ad = final_ad[i]
        rest_time = sum(path_time[i-1:])
        print(rest_time)
        eel.next_data(current_ad, str(rest_time))
    elif i == path_size -1:
        eel.last_page()

@eel.expose
def before_path():
    global path_size
    global i
    global final_ad
    global path_time

    print("i", i)
    if i > 1:
        i += -1

        current_ad = final_ad[i]
        rest_time = sum(path_time[i-1:])
        print(rest_time)
        eel.before_data(current_ad, str(rest_time))

@eel.expose
def b_check():
    if i != 1:
        eel.hide()
        
@eel.expose
def on_page2_load():
    ###load pickle 필요
    # global ad1_list
    # global ad2_list
    # global ad3_list
    #
    # ad1_list = recent1
    # ad2_list = recent2
    # ad3_list = recent3
    print("여기!")
    ad_pack = [recent1,recent2,recent3]
    eel.change(ad_pack)


@eel.expose
def to_calculate(num):
    ###recent pickle로 불러오기

    global addressList

    if num == 3:
        addressList = recent3
    elif num == 2:
        addressList = recent2
    else:
        addressList = recent1

    eel.to_page_3()



say_hello_py('Python World!')
eel.say_hello_js('Python World!')  # Call a Javascript function

eel.start('/page1.html', size=(1280, 832))  # Start
