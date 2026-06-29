from tkinter import *

root = Tk()
root.title("Nado GUI")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제")
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame=Frame(root)
list_frame.pack(fill="both")
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y") # fill y : 세로 공간을 꽉 채움(스크롤)

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set) # extended: 다중 선택 허용 / yscrollcommand: 리스트박스에 스크롤바 연동
list_file.pack(side="left", fill="both", expand=True) # both: 가로세로 , expend: 남은 공간 모두 확장
scrollbar.config(command=list_file.yview) # 스크롤에 리스트박스 매핑

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack()

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4) # iapy: 높이 조정

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right")

root.resizable(False, False)
root.mainloop()