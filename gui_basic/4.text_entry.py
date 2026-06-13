from tkinter import *

root = Tk() # Tk 인스턴스 생성 및 할당
root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 프로그램 창 크기 설정 (가로 * 세로)

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요") # 글자 삽입(기본값)

e = Entry(root, width=30)
e.pack()

e.insert(0, "한 줄만 입력해요") # 1번째 매개변수: 글자 인덱스 위치, 2번째 매개변수: 범위 최종 위치

# 버튼 클릭으로 조작

## Text 읽기
btn1 = Button(root, text="Text 출력", command=lambda: print(txt.get("1.0", END))) # 1번째 매개변수: 라인 / 2번째 매개변수: 컬럼 (익명함수로 콜백함수 처리)
btn1.pack()

## Entry 읽기
btn2 = Button(root, text="Entry 출력", command=lambda: print(e.get()))
btn2.pack()

def btncmd(): 
  txt.delete("1.0", END)
  e.delete(0, END) # 1번째 매개변수: 글자 인덱스 위치, 2번째 매개변수: 범위 최종 위치

btn3 = Button(root, text="모두 삭제", command=btncmd)
btn3.pack()

root.mainloop()