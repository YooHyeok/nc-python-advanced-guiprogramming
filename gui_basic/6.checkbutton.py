from tkinter import *

root = Tk() # Tk 인스턴스 생성 및 할당
root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 프로그램 창 크기 설정 (가로 * 세로)

chkvar = IntVar() # 체크여부 확인용 값
checkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
checkbox.select() # 선택 처리
checkbox.deselect() # 선택 해제
checkbox.pack()

chkvar2 = IntVar()
checkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
checkbox2.pack()

def btncmd():
  print(chkvar.get()) # 체크 여부 조회: 0=해제, 1=체크
  print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()