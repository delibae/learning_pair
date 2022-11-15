import pandas as pd
import time
import random

addressList = []
for i in range(100):
    addressList.append(i)
addressList2 = []
for i in range(200):
    addressList2.append(i)


# serialNumList = []
address_dict = {}
for i in range(len(addressList2)):
    address_dict[i] = i
# # 전체주소-전체주소: 소요시간
time_dict = {}

for i in range(len(addressList2)):
    for j in range(i+1,len(addressList2)):
        time_dict[f'{i}-{j}'] = random.randint(1,100)

class Graph():
    def __init__(self, size, addressList, address_dict, time_dict):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

        self.address_dict = address_dict
        self.time_dict = time_dict
        self.addressList = addressList
        self.serialNumList = []

        for i in range(len(self.addressList)):
            if self.addressList[i] in self.address_dict:
                self.serialNumList.insert(i, self.address_dict[self.addressList[i]])

        for i in range(len(self.serialNumList)):
            for j in range(i, len(self.serialNumList)):
                self.add(i, j)

    def add(self, i, j):
        if i == j:
            self.graph[i][j] = 999
        else:
            try:
                time = self.time_dict[str(self.serialNumList[i]) + "-" + str(self.serialNumList[j])]
            except:
                time = self.time_dict[str(self.serialNumList[j]) + "-" + str(self.serialNumList[i])]
            self.graph[j][i] = time
            self.graph[i][j] = time

    def out(self):
        for i in self.graph:
            print(i)


# 일련번호 리스트 이용해서 그래프 만들기
# routeGraph = Graph(len(addressList), addressList, address_dict, time_dict)


class frm():
    def __init__(self,routeGraph, n , pivot, serialNumList):
        self.routeGraph = routeGraph
        self.n = n
        self.pivot = pivot

        self.serialNumList = serialNumList

        self.path = []
        self.path_time = []
        self.path.append(self.pivot)

        self.for_visit = [0 for i in range(self.routeGraph.SIZE)]
        self.for_visit[self.pivot] = 1

        self.Graph_to = pd.DataFrame(self.routeGraph.graph)

        self.seq_n, self.seq_rest = self.seq_in()

    def seq_in(self):
        if (self.routeGraph.SIZE - 1)%self.n == 0:
            seq_n = (self.routeGraph.SIZE -1)//self.n
            seq_rest = None
        else:
            seq_n = (self.routeGraph.SIZE -1)//self.n
            seq_rest = (self.routeGraph.SIZE - 1)%self.n
        return seq_n,seq_rest


    def pp(self,ary, num):
        result = []
        if num >= 1:
            for i in ary:
                arr = ary.copy()
                arr.remove(i)
                get = self.pp(arr,num-1)
                for j in get:
                    result.append([i]+j)
        if num == 1:
            for i in ary:
                result.append([i])
            return result
        return result

    def find_min(self,num):
        r = []
        for i in range(len(self.for_visit)):
            if self.for_visit[i] == 0:
                r.append(i)
        min = 9999
        min_pth = None
        min_time = None

        for i in self.pp(r, num):
            point = self.pivot
            total = []
            for j in i:
                total.append(self.Graph_to.loc[point, j])
                point = j
            if sum(total) < min:
                min = sum(total)
                min_pth = i
                min_time = total

        self.path.extend(min_pth)

        self.path_time.extend(min_time)
        self.pivot = self.path[-1]
        for i in min_pth:
            self.for_visit[i] = 1

    def complete_path(self):
        for i in range(self.seq_n):
            self.find_min(self.n)
        if self.seq_rest != None:
            self.find_min(self.seq_rest)
        #path to seriul num
        seriul_path = []
        for i in self.path:
            seriul_path.append(self.serialNumList[i])
        self.path = seriul_path
        return self.pivot, self.path, self.path_time

#
# pivot = address_dict.get(addressList[0])
# n = 2
# a = frm(routeGraph,n,pivot,routeGraph.serialNumList)
#
# pivot, path, path_time = a.complete_path()
# print(routeGraph.serialNumList)
# print(path)
# print(path_time)
#
# convert_address_dict = {v:k for k,v in address_dict.items()}

def serial_to_ad(path,convert_address_dict):
    f_ad = []
    for i in path:
        f_ad.append(convert_address_dict.get(i))
    return f_ad



# print(convert_address_dict)
# print(serial_to_ad(path))

# def cl_1000():
#     start = time.time()
#     b = []
#     list = [1]
#     for i in range(10000):
#         a = list[0] > list[0]
#         b.append(a)
#     close = time.time()
#     return (close - start)
#
# print(cl_1000())

def factorial(n):
    re = 1
    for i in range(1, n+1):
        re *= i
    return re

def sum_calculate(i,n):
    total = 0
    for m in range((i-1)//n):
        total += factorial(i-1-n*m)/factorial(i-1-n*m-n)
    if (i-1)%n != 0:
        total += factorial((i-1)%n)
    return total
print(sum_calculate(10,1))

def find_n(i,target,time_gap,time1):
    standard_time = 0.01
    t_weight = round(0.01/time_gap)
    if t_weight == 0:
        t_weight = 1
    print("t_weight :" , t_weight)
    weight = i
    if i >= 150:
        max_n = 1*t_weight
    elif i >= 50:
        max_n = 2*t_weight
    elif i >= 20:
        max_n = 3*t_weight
    elif i >= 10:
        max_n = 4
    else:
        max_n = 999
    print("weight: ",weight)
    load_time = weight*time1
    print("loda_time: ",load_time)

    if time_gap > 0:
        num1 = sum_calculate(100,10)
        num2 = sum_calculate(200,10)
        gap = num2 - num1
        unit_time = (time_gap/gap)*weight
        target = target - load_time
        print("target: ",target)
        max_cal = target//unit_time + num1
        print("max_cal: ", max_cal)
        for j in range(1,i):
            if sum_calculate(i,j) > max_cal:
                if j > max_n:
                    return max_n
                return j

        if i-1 > max_n:
            return max_n
        return i-1

    else:
        if i-1 > max_n:
            return max_n
        return i-1




def get_time_gap():
    routeGraph1 = Graph(len(addressList), addressList, address_dict, time_dict)
    routeGraph2 = Graph(len(addressList2), addressList2, address_dict, time_dict)
    pivot = address_dict.get(addressList[0])
    ### n 값 결정 알고리즘 필요
    n = 1
    a = frm(routeGraph1, n, pivot, routeGraph1.serialNumList)
    n = 10
    start = time.time()
    a = frm(routeGraph1, n, pivot, routeGraph1.serialNumList)
    time1 = time.time() - start
    print("time1: ", time1)
    n = 10
    start = time.time()
    a = frm(routeGraph2, n, pivot, routeGraph2.serialNumList)
    time2 = time.time() - start
    print("time2: ", time2)
    time_gap = time2 - time1
    print("time_gap: ", time_gap)

    return time_gap, time1

# time_gap,time1 = get_time_gap()
# print(find_n(100,2,time_gap,time1))
