from tkinter import *

root = Tk() # Tk 인스턴스 생성 및 할당
root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 프로그램 창 크기 설정 (가로 * 세로)

"""
Listbox: 여러가지 값을 관리 하는 목록 위젯
selectmode :  extended=여러개 선택 가능 / single=한개만 선택 가능
height : 목록 높이 - 0=모든 목록 출력, 실제 목록보다 낮을경우 키보드 상하 키로 이동/출력 가능하다.
"""
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") # 맨 뒤에 항목 추가
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
  listbox.delete(END) # 가장 마지막 항목 삭제
  listbox.delete(0) # 가장 첫번째 항목 삭제

  # 갯수 확인
  print("리스트에는 ", listbox.size(), "개가 있어요.")

  # 항목 학인 - get(시작index, 끝index)
  print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))
  # 선택된 항목 확인 - curselection() : 선택된 항목의 인덱스 값 반환
  print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()