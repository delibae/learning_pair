import pandas as pd
import time
import random

addressList = []
for i in range(100):
    addressList.append(i)

# serialNumList = []
address_dict = {}
for i in range(len(addressList)):
    address_dict[i] = i
# # 전체주소-전체주소: 소요시간
time_dict = {}

for i in range(len(addressList)):
    for j in range(i+1,len(addressList)):
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

def find_n(i,target):
    routeGraph = Graph(len(addressList), addressList, address_dict, time_dict)
    pivot = address_dict.get(addressList[0])
    ### n 값 결정 알고리즘 필요
    n = 1
    a = frm(routeGraph, n, pivot, routeGraph.serialNumList)
    n = 1
    start = time.time()
    a = frm(routeGraph, n, pivot, routeGraph.serialNumList)
    time1 = time.time() - start
    print(time1)
    n = 10
    start = time.time()
    a = frm(routeGraph, n, pivot, routeGraph.serialNumList)
    time2 = time.time() - start
    print(time2)
    time_gap = time2 - time1
    print(time_gap)
    if time_gap > 0:
        num1 = sum_calculate(100,1)
        num2 = sum_calculate(100,10)
        gap = num2 - num1
        unit_time = time_gap/gap

        max_cal = target//unit_time

        for j in range(1,i):
            if sum_calculate(i,j) > max_cal:
                 return j
        return i-1

    else:
        return i-1


