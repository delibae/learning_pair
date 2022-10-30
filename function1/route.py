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
addressList = ['Loc1','Loc2','Loc5']
serialNumList = [] # 일련번호 리스트

# 일련번호 리스트 채우기
for i in range(len(addressList)):
    if addressList[i] in address_dict:
        serialNumList.insert(i,address_dict[addressList[i]])

class Graph():
    def __init__(self,size): 
        self.SIZE = size
        self.graph = [[0 for _ in range(size)]for _ in range(size)]

# 일련번호 리스트 이용해서 그래프 만들기
routeGraph = Graph(len(serialNumList))

for i in range (len(serialNumList)):
    for j in range (len(serialNumList)):
        if i == j:
            routeGraph.graph[i][j] = 999
        else:
            route = str(serialNumList[i])+"-"+str(serialNumList[j])
            if route not in time_dict:
                routeGraph.graph[i][j] = time_dict[str(serialNumList[j])+"-"+str(serialNumList[i])]
            else:
                routeGraph.graph[i][j] = time_dict[str(serialNumList[i])+"-"+str(serialNumList[j])]
        #print(routeGraph.graph[i][j])

# 경로 생성

checkPoint = "Loc2"
checkPointNum = address_dict[checkPoint]
nextNum = 0

shortRoute = 999

visited = [checkPointNum]

# 큐형식으로 작업 공간 생성
current = []
originCurrent =[]
def creating_queue (pointNum):
    global current
    global originCurrent
    current = []
    originCurrent = []
    for i in serialNumList:
        current.append(routeGraph.graph[serialNumList.index(pointNum)][serialNumList.index(i)])
        originCurrent.append(routeGraph.graph[serialNumList.index(pointNum)][serialNumList.index(i)])
    for j in visited:
        print("방문 :", j)
        current.remove(routeGraph.graph[serialNumList.index(pointNum)][serialNumList.index(j)])
        print("커런트 : ",current)




# 다익스트라 알고리즘 사용
for i in range(len(serialNumList)-1):
    #print(i)
    creating_queue(checkPointNum)
    for i in current:
        if shortRoute > i:
            shortRoute = i
    print("오리진 : ",originCurrent)
    visited.append(serialNumList[originCurrent.index(shortRoute)])
    checkPointNum = serialNumList[originCurrent.index(shortRoute)]
    shortRoute=999

    print(visited)




#1s

# 변경 사항: 경로 설정 완료
# 최종 보고서때 까지 작업 해야하는 사항: 엑셀 파일 가져오기, 화면 출력
