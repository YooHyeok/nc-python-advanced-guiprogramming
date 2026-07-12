from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from pathlib import Path # 추가
from PIL import Image # 추가
import os # 추가

BASE_DIR = Path(__file__).resolve().parent # 현재 파일이 있는 디렉토리
SAMPLE_DIR = BASE_DIR / "sample" # 샘플 이미지 디렉토리
SAVE_DIR = BASE_DIR / "save" # 샘플 이미지 디렉토리

root = Tk()
root.title("Nado GUI")

# 저장경로 (폴더)
def browse_dest_path():
  folder_selected = filedialog.askdirectory(initialdir=SAVE_DIR) # 폴더 선택 후 반환받은 폴더 경로 저장
  if folder_selected == None: # 사용자가 취소를 누를 때
    return
  # print(folder_selected)
  txt_dest_path.delete(0, END) #  경로 초기화(Entry 이므로 0부터 끝까지 삭제)
  txt_dest_path.insert(0, folder_selected) #  선택된 경로 삽입

# 이미지 통합
def merge_image():

  print("가로넓이 : ", cmb_width.get())
  print("간격 : ", cmb_space.get())
  print("포맷 : ", cmb_format.get())

  # 가로 넓이
  img_width = cmb_width.get()
  if img_width == "원본 유지":
    img_width = -1 # -1일 때는 원본 기준
  else:
    img_width = int(img_width)

  # 간격
  img_space = cmb_space.get()
  if img_space == "좁게":
    img_space = 30
  elif img_space == "보통":
    img_space = 60
  elif img_space == "넓게":
    img_space = 90
  else: # 없을 경우
    img_space = 0

  # 포맷
  img_format = cmb_format.get().lower() # PNG, JPG, BMP 값을 받아와서 소문자로 변경

  ################################################################

  images = [Image.open(x) for x in list_file.get(0, END)] # 이미지 객체 저장

  # 이미지 사이즈 리스트에 넣어 하나씩 처리
  image_sizes = [] # (width1, height1), (width2, height2)
  if img_width > -1:
    # width 값 변경
    """
    비율 계산식
    100 * 60 → width = 80 ↓ : height?
    (원본 width : 원본 height) = (변경 width : 변경 height)
    x : y = x' : y'
    xy' = yx'
    y = yx' / x
    100 : 60 = 80 : 48
    
    x = width = size[0]
    y = height = size[1]
    x' = img_width # 해당 값으로 변경해야 함
    y' = x'y / x = (img_width * size[1]) / size[0]
    """
    image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
    print("image_sizes = ", image_sizes)
  else:
    # 원본 사이즈 사용
    image_sizes = [(x.size[0], x.size[1]) for x in images]
  

  # size → size[0] : width, size[1] : height
  # zip(*)을 이용해 이미지 배열에서 가로·세로 크기를 한 번에 분리 및 추출
  # widths, heights = zip(*[x.size for x in images]) 
  widths, heights = zip(*(image_sizes)) 
  print("widths = ", widths)
  print("heights = ", heights)

  max_width, total_height = max(widths), sum(heights)
  # 스케치북 준비
  
  if img_space > 0: # 이미지 간격 옵션 적용
    total_height += (img_space * (len(images) - 1))

  result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) # 배경 흰색
  y_offset = 0 # 이미지가 첨부될 Y 위치(이미지가 첨부될때마다 동적으로 변경됨)
  for idx, img in enumerate(images):
    # width가 원본유지가 아닐 경우 이미지 크기 조정
    if img_width > -1:
      img = img.resize(image_sizes[idx])

    result_img.paste(img, (0, y_offset))
    y_offset += (img.size[1] + img_space) # 현재 추가된 image의 높이값을 누적 + 사용자가 지정한 간격

    # progress 계산(percent)
    progress = (idx + 1) / len(images) * 100
    p_var.set(progress)
    progress_bar.update()

  # 포맷 옵션 처리
  file_name = "nado_photo." + img_format
  dest_path = os.path.join(txt_dest_path.get(), file_name)
  result_img.save(dest_path)
  msgbox.showinfo("알림", "작업이 완료되었습니다.")

# 시작: 병합작업(파일목록, 저장경로, 옵션 정보 기준)
def start():
  # 각 옵션들 값을 확인
  # print("가로넓이 : ", cmb_width.get())
  # print("간격 : ", cmb_space.get())
  # print("포맷 : ", cmb_format.get())

  # 파일 목록 조회
  if list_file.size() == 0:
    msgbox.showwarning("경고", "이미지 파일을 추가하세요")
    return
  # 저장 경로 확인
  if len(txt_dest_path.get()) == 0:
    msgbox.showwarning("경고", "저장 경로를 선택하세요")
    return
  # 이미지 통합 작업
  merge_image()



# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) 

# 파일 추가/ 선택 삭제 버튼 배치 및 기능 구현
## 파일 추가 - askopenfilenames(): 복수개 파일 선택 함수
def add_file():
  files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
                                      filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), # 튜플형태로 여러 파일 타입 수용 
                                      # initialdir="C:/" # 기본 경로
                                      initialdir=SAMPLE_DIR # 현재 파일 기준 sample 디렉토리
  ) 
  # 사용자가 선택한 파일 목록에 추가
  for file in files:
    list_file.insert(END, file) # 리스트 마지막에 순차적으로 추가

## 선택 삭제
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

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
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

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()
