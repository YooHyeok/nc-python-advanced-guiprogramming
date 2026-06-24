import tkinter.messagebox as msgbox
from tkinter import *

root = Tk() # Tk 인스턴스 생성 및 할당
root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 프로그램 창 크기 설정 (가로 * 세로)

btn1 = Button(root, text="버튼1")
btn2 = Button(root, text="버튼2")

# 버튼배치 예제

## 기본 pack을 통한 배치
# btn1.pack()
# btn2.pack()

# btn1.pack(side="left") # 좌측에 배치
# btn2.pack(side="right") # pack() = 쌓는 느낌

## grid에 배치(지정된 좌표 위치에 배치)
# btn1.grid(row=0, column=0) # grid의 0행 0열에 배치
# btn2.grid(row=1, column=1) # grid의 1행 1열에 배치

# 계산기 예제
## 1번째 줄 정의 및 배치
# btn_f16 = Button(root, text="F16", padx=10, pady=10) # pad옵션: 글짜 기준 x=상하/y=좌우 크기 조절
btn_f16 = Button(root, text="F16", width=5, height=2) # width/height: 고정 너비/높이
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3) # sticky옵션을 통해 상하좌우 빈 공간 영역 확보
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3) # pad옵션: 글짜 기준 x=상하/y=좌우 크기 조절(3만큼 )
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

## 2번째 줄 정의 및 배치
btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

## 3번째 줄 정의 및 배치
btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

## 4번째 줄 정의 및 배치
btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_add = Button(root, text="-", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

## 5번째 줄 정의 및 배치
btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # 셀 세로 병합: rowspan(현재 위치로부터 N줄을 병합)

btn_0 = Button(root, text="0", width=5, height=2)
btn_point = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()