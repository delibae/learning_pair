# 전체 주소:일련번호
from tracemalloc import start


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

# 출발지 설정 (현재는 테스트 값)
startPoint = "Loc1"
startSerialNumberIndex = serialNumList.index(address_dict[startPoint])
shortRoute = 999

visited = [address_dict[startPoint]] # 방문 여부
print(visited)
while len(visited) != len(serialNumList):
    for i in range(len(serialNumList)):
        if shortRoute > routeGraph.graph[startSerialNumberIndex][i]:
            print(i)
            shortRoute = routeGraph.graph[startSerialNumberIndex][i]
            print(shortRoute)
            visited.append(serialNumList[i])
            print(visited)
    startSerialNumberIndex = i
# 문제점 최단 루트를 다시 초기화 하는데 있어서 문제가 있다. 
# 갔었던 루트는 다시 택하면 안되지만 다시 택하는 문제점이 있음
# 중간 보고서때 까지 작업 해야하는 사항: 문제점 해결

#def dijkstra (start):

# 최종 보고서때 까지 작업 해야하는 사항: 엑셀 파일 가져오기, 화면 출력