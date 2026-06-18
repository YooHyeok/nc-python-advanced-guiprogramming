import tkinter.ttk as ttk
from tkinter import *

root = Tk() # Tk 인스턴스 생성 및 할당
root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 프로그램 창 크기 설정 (가로 * 세로)

values = [str(i) + "일" for i in range(1, 32) ] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
  print(combobox.get()) # 선택된 값 표시
  print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop()