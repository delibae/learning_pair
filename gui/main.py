import eel
import pandas as pd
import json
from pandas import json_normalize
import route_module as rt
import time

addressList = ['Loc0', 'Loc1', 'Loc2', 'Loc3']
serialNumList = []

address_dict = {'Loc0': 0, 'Loc1': 1, 'Loc3': 2, 'Loc4': 3, 'Loc5': 4}
# 전체주소-전체주소: 소요시간
time_dict = {'0-1': 30, '0-2': 40, '0-3': 10, '0-4': 90, '1-2': 60, '1-3': 80, '1-4': 25, '2-3': 5, '2-4': 15,
             '3-4': 45}

convert_address_dict = {v:k for k,v in address_dict.items()}

# Set web files folder
eel.init('web')

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

@eel.expose
def get_file(file):
    print(type(file))
    info = json.loads(file)
    df = json_normalize(info)
    global ad_list
    ad_list = df['도로명']
    print(ad_list)

#ad_list => address_list 전환 필요
@eel.expose
def find_path():
    routeGraph = rt.Graph(len(addressList), addressList, address_dict, time_dict)
    pivot = address_dict.get(addressList[0])
    #n 값 결정 알고리즘 필요
    n = 2
    a = rt.frm(routeGraph, n, pivot)

    global path_time
    pivot, path, path_time = a.complete_path()

    global final_ad
    final_ad = rt.serial_to_ad(path)
    print(final_ad)

    eel.check()

    # 나중에 지울것
    time.sleep(3)

    eel.next_page()


i = 0
@eel.expose
def next_path():
    global path_size
    global i

    i += 1

    path_size = len(path_time)

    current_ad = final_ad[i]
    rest_time = sum(path_time[i+1:])


say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

eel.start('/page1.html', size=(1280, 832))  # Start
