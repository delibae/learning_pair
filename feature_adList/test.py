bf = []

while True:
    print("-"*30)
    print("- Best Friend 적어보기 -\n1. 베프 이름 출력\n2.베프 이름 추가\n3.베프 이름 삭제\n0. 프로그램 종료")
    print()
    a = input("메뉴 선택>> ")
    if a == "1":
        if len(bf) > 0:
            print(bf)
        else:
            print("아직 추가한 베프가 없습니다.")
            
    elif a == "2":
        b = input("베프 이름 입력>> ")
        bf.append(bf)
    
    elif a == '3':
        c = input("삭제하고 싶은 베프 이름 입력>> ")
        bf.remove(c)
        
    elif a == "0":
        break
    
    else:
        print("메뉴 선택 다시")
