# 전체 주소:일련번호
import queue
from tabnanny import check
from tracemalloc import start

from numpy import Inf


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

def seq_in(routeGraph, n):
    if (routeGraph.SIZE - 1)%n == 0:
        seq_n = (routeGraph.SIZE -1)//2
        seq_rest = None
    else:
        seq_n = (routeGraph.SIZE -1)//2
        seq_rest = (routeGraph.SIZE - 1)%n
    return seq_n,seq_rest


def pp(ary, num):
    result = []
    if num >= 1:
        for i in ary:
            arr = ary.copy()
            arr.remove(i)
            get = pp(arr,num-1)
            for j in get:
                result.append([i]+j)
    if num == 1:
        for i in ary:
            result.append([i])
        return result
    return result

def find_min(Graph_to, for_visit, pivot, num, path, path_time):
    r = []
    for i in range(len(for_visit)):
        if for_visit[i] == 0:
            r.append(i)
    min = 9999
    min_pth = None
    min_time = None

    for i in pp(r, num):
        point = pivot
        total = []
        for j in i:
            total.append(Graph_to.loc[point, j])
            point = j
        if sum(total) < min:
            min = sum(total)
            min_pth = i
            min_time = total

    path.extend(min_pth)

    path_time.extend(min_time)
    pivot = path[-1]
    for i in min_pth:
        for_visit[i] = 1
    return  pivot, path, path_time

def complete_path(routeGraph, n , pivot):
    path = []
    path_time = []
    path.append(pivot)

    for_visit = [0 for i in range(routeGraph.SIZE)]
    for_visit[pivot] = 1
    Graph_to = pd.DataFrame(routeGraph.graph)

    seq_n , seq_rest = seq_in(routeGraph,n)
    for i in range(seq_n):
        pivotm, path, path_time = find_min(Graph_to, for_visit, pivot,n, path, path_time)
    if seq_rest != None:
        pivot, path, path_time = find_min(Graph_to, for_visit, pivot,seq_rest, path, path_time)
    return pivot, path, path_time


pivot = 0
n = 2

pivot, path, path_time = complete_path(routeGraph,n,pivot)
print(path)
