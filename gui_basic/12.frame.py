import tkinter.messagebox as msgbox
from tkinter import *

root = Tk() # Tk 인스턴스 생성 및 할당
root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 프로그램 창 크기 설정 (가로 * 세로)

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1) # 프레임 : 
# frame_burger.pack(side="left") # 좌측 배치 출력
# frame_burger.pack(side="left", fill="both") # 좌측 배치, 상하 영역 확보 출력
frame_burger.pack(side="left", fill="both", expand=True) # 좌측 배치, 상하, 좌우 영역 확보 출력

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text="음료") # 라벨, 제목 지정
# frame_drink.pack(side="right", ) # 우측 배치 출력
# frame_drink.pack(side="right", fill="both") # 우측 배치, 상하 영역 확보 출력
frame_drink.pack(side="right", fill="both", expand=True) # 우측 배치, 상하, 좌우 영역 확보 출력
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop()