import tkinter.messagebox as msgbox
from tkinter import *

root = Tk() # Tk 인스턴스 생성 및 할당
root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 프로그램 창 크기 설정 (가로 * 세로)

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") # 좌측 배치, y축 영역 확보.

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set) # yscrollcommand: scrollbar 매핑 - scrollbar.set이 없으면 스크롤을 내려도 다시 올라옴.
for i in range(1, 32): # 1 ~ 31 일 범위
  listbox.insert(END, str(i) + "일") # 1일, 2일, ...
listbox.pack()

scrollbar.config(command=listbox.yview) # listbox에 y축 스크롤 매핑

root.mainloop()