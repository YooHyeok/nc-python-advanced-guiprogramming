from tkinter import *

root = Tk() # Tk 인스턴스 생성 및 할당
root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img/check.png")
label2 = Label(root, image=photo)
label2.pack()

# 레이블 동적 업데이트 : 버튼 클릭시 텍스트 변경
def change():
  label1.config(text="또 만나요")
  global photo2
  photo2 = PhotoImage(file="gui_basic/img/x.png")
  label2.config(image=photo2)
btn = Button(root, text="클릭", command=change)
btn.pack()



root.mainloop()