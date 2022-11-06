# learning_pair
## 전체
### Branch
feature/selenium1<br/>
feature/root<br/>
root/root1<br/>
feature/address<br/>
feature/gui<br/>


### To Do
1. 지역 내에 이동 포인트 선정 및 리스트화<br/><br/>
2. 셀레니움 이용하여 포인트간의 경로 시간 데이터 불러오는 코드 작성<br/><br/>
3. 경로 시간 이름을 어떻게 정할건지 결정<br/><br/>
4. 크롤링한 결과를 형식에 맞게 csv형태로 저장<br/><br/>
5. csv형태로 저장한 결과를 hash map을 통해 database화 <br/>
ㄴ 파이썬 기본 dictionary가 hash map 형태이므로 이를 pickle 파일로 저장<br/><br/>
6.  사용자가 선정한 핀포인트들의 데이터를 database에서 호출후 dictionary 형태로 저장<br/><br/>
7. 동적불한 greedy 및 여러 알고리즘을 이용하여 모든 경우의 수 판단하지 않고 빠른 시간내에 결과값 도출<br/><br/>
8. 6,7에서의 input과 7에서의 output을 입출력하는 gui 제작<br/><br/>

### 분업 시나리오
1단계<br/><br/>
파트 1: 셀레니움을 통한 데이터 크롤링<br/><br/>
파트 2: 가상의 데이터 설정후 이에 대해서 최단경로를  계산하는 알고리즘 작성<br/><br/>
파트 3: 핀포인트 설정 및 리스트화(key: 주소 / value: 좌표)<br/>
ㄴ 필요에 따라서 핀포인트를 좌표를 기준으로 자동으로 설정하고 이에 대해서 주소를 크롤링 하는 방식도 필요할듯<br/><br/>
2단계<br/><br/>
파트1: 입출력 gui 제작<br/><br/>

### 협업 규칙

1. 각자의 브랜치에서 담당한 기능을 만든후 merge 해주세요<br/><br/>

2. pull request 요청시에 리뷰하고 comment 남겨주세요 <br/><br/>

3. branch 명은 feature/기능명 => 기능명/세부기능 과 같이 하위 브랜치를 생성해주세요<br/><br/>

4. 본인이 생성한 branch는 항상 최신화 하여 README.md에 정리해주세요(꼭 master에!!)<br/><br/>


## 한진
### Complete

1. 협업 규칙 및 개발 가이드라인 작성
2. selenium4 immigration 완료 및 크롤링 코드작성 완료
3. 중간 단계 코드 점검 완료

### To Do

### 명섭
### Complete
### To Do

### 수민
### Complete
### To Do