# 전체 주소:일련번호
import queue
from tabnanny import check
from tracemalloc import start

from numpy import Inf
import pickle

# pickle 로드 파트 크롤링 완료후 연결
# with open("time_dict1.pickle","rb") as fr:
#     data = pickle.load(fr)
# print(data)
# with open("address_dict.pickle","rb") as fr:
#     data2 = pickle.load(fr)
# print(data2)

address_dict = {'Loc1':1,'Loc2':2,'Loc3':3,'Loc4':4,'Loc5':5}
# 전체주소-전체주소: 소요시간
time_dict = {'1-2':30,'1-3':40,'1-4':10,'1-5':90,'2-3':60,'2-4':80,'2-5':25,'3-4':5,'3-5':15,'4-5':45}


enterType = False
# false 일 때가 화면 터치, true 일때가 엑셀 파일

# 파일 입력 부분은 최종 보고서시 작성

# 입력 받은 리스트 (현재는 테스트 값)
addressList = ['Loc1','Loc2','Loc4','Loc5']
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
    def out(self):
        for i in self.graph:
            print(i)


# 일련번호 리스트 이용해서 그래프 만들기
routeGraph = Graph(len(serialNumList))

for i in range (len(serialNumList)):
    for j in range (i, len(serialNumList)):
        routeGraph.add(i,j)



import time
import datetime
import pandas as pd

# start = time.time()
#
# for i in range(10000000):
#     a = 2021 > 2020
#
# sec = time.time() -start
#
# times = str(datetime.timedelta(seconds=sec))
# print(times)



class frm():
    def __init__(self,routeGraph, n , pivot):
        self.routeGraph = routeGraph
        self.n = n
        self.pivot = pivot

        self.path = []
        self.path_time = []
        self.path.append(self.pivot)

        self.for_visit = [0 for i in range(self.routeGraph.SIZE)]
        self.for_visit[self.pivot] = 1

        self.Graph_to = pd.DataFrame(self.routeGraph.graph)

        self.seq_n, self.seq_rest = self.seq_in()

    def seq_in(self):
        if (self.routeGraph.SIZE - 1)%n == 0:
            seq_n = (self.routeGraph.SIZE -1)//n
            seq_rest = None
        else:
            seq_n = (self.routeGraph.SIZE -1)//n
            seq_rest = (self.routeGraph.SIZE - 1)%n
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
        return self.pivot, self.path, self.path_time

pivot = 0
n = 2
a = frm(routeGraph,n,pivot)
pivot, path, path_time = a.complete_path()
print(path)
print(path_time)









