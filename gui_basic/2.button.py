from tkinter import *

root = Tk() # Tk 인스턴스 생성 및 할당
root.title("Nado GUI") # 프로그램 창 타이틀

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, padx=10, pady=5, text="버튼33333333333333333333333")
btn4.pack()

btn5 = Button(root, width=10, height=3, text="버튼4")
btn5.pack()
btn6 = Button(root, width=10, height=3, text="버튼44444444444444444444444") # width/heigh = t고정크기
btn6.pack()

btn7 = Button(root, fg="red", bg="yellow", text="버튼5")
btn7.pack()

# 이미지 타입 버튼
photo = PhotoImage(file="gui_basic/img/check.png")
btn8 = Button(root, image=photo)
btn8.pack()

# command - 버튼 동작
def btncmd():
  print("버튼이 클릭되었어요")
btn9 = Button(root, text="동작하는 버튼", command=btncmd)
btn9.pack()

root.mainloop()