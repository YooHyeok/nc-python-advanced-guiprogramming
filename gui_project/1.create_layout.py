from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # x축 기준 간격 펼치기 / A) 간격 띄우기 - pad

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제")
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame=Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y") # fill y : 세로 공간을 꽉 채움(스크롤)

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set) # extended: 다중 선택 허용 / yscrollcommand: 리스트박스에 스크롤바 연동
list_file.pack(side="left", fill="both", expand=True) # both: 가로세로 , expend: 남은 공간 모두 확장
scrollbar.config(command=list_file.yview) # 스크롤에 리스트박스 매핑

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=4) # 저장경로 x축 기준 간격 펼치기 / B) 프레임 높이 조정 - ipad

txt_dest_path = Entry(path_frame, width=50)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # iapy: 높이 조정 / A) 간격 띄우기 - pad

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=4) # B) 프레임 높이 조정 - ipad

## 가로 넓이 옵션
### 가로 넓이 라벨
Label(frame_option, text="가로넓이", width=8).pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad
### 가로 넓이 콤보
opt_width=["원본 유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad
## 간격 옵션
### 간격 옵션 라벨
Label(frame_option, text="간격", width=8).pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad
opt_space=["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad
### 간격 옵션 라벨

## 파일 포맷 옵션
Label(frame_option, text="포맷", width=8).pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad
opt_format=["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad

## 진행상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=4) # B) 프레임 높이 조정 - ipad / B) 프레임 높이 조정 - ipad

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5) # A) 간격 띄우기 - pad

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5) # A) 간격 띄우기 - pad

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12)
btn_start.pack(side="right", padx=5, pady=5) # A) 간격 띄우기 - pad

root.resizable(False, False)
root.mainloop()