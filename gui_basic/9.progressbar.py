import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk() # Tk 인스턴스 생성 및 할당
root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 프로그램 창 크기 설정 (가로 * 세로)

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # indeterminate: 종료가 결정되지 않은 옵션(좌우로 이동)
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.start(10) # 10ms 마다 움직임.
progressbar.pack()

def btncmd():
  progressbar.stop() # 작동 중지

btn = Button(root, text="중지", command=btncmd)
btn.pack()


p_var2 = DoubleVar() # 항상 정수값으로 올라가지 않기 위해(실수) Double 적용
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
  for i in range(1, 101): # 1 ~ 100 까지 값
    time.sleep(0.01) # 0.01초 대기
    p_var2.set(i) # 0부터 100까지의 값을 할당
    progressbar2.update() # ui 업데이트
    print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()


root.mainloop()