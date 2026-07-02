from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) 

# 파일 추가/ 선택 삭제 버튼 배치 및 기능 구현
# A) 파일 추가 - askopenfilenames(): 복수개 파일 선택 함수
def add_file():
  files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
                                      filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), # 튜플형태로 여러 파일 타입 수용 
                                      initialdir="C:/" # 기본 경로
  ) 
  # 사용자가 선택한 파일 목록에 추가
  for file in files:
    list_file.insert(END, file) # 리스트 마지막에 순차적으로 추가

# B) 선택 삭제
def del_file():
  for index in reversed(list_file.curselection()): # 거꾸로 제거해야하는 이유 : 예를들어 0번을 제거하고나면 1번이 0번 위치로 이동하게됨. 이상태에서 1번을 제거하면 원조 1번이 아닌 기존 2번이 제거됨. 최종 결과적으로 마지막에 0번 위치에 5번 데이터가 오는데 5번 인덱스를 지워도 해당 데이터는 남게됨.
  # for index in list_file.curselection():
    print(index)
    list_file.delete(index) # Listbox로 부터 현재 선택된 아이템 제거
  
btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame=Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=4)

txt_dest_path = Entry(path_frame, width=50)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=4)

## 가로 넓이 옵션
### 가로 넓이 라벨
Label(frame_option, text="가로넓이", width=8).pack(side="left", padx=5, pady=5)
### 가로 넓이 콤보
opt_width=["원본 유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)
## 간격 옵션
### 간격 옵션 라벨
Label(frame_option, text="간격", width=8).pack(side="left", padx=5, pady=5)
opt_space=["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

## 파일 포맷 옵션
### 파일 포맷 옵션 라벨
Label(frame_option, text="포맷", width=8).pack(side="left", padx=5, pady=5)
opt_format=["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

## 진행상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=4)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()