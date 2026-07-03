# [루트/README.md](../../README.md)
# [기본기](../../gui_basic/docs/README.md)

# 이미지 병합 GUI 프로그램

## [사용자 시나리오]
1. 사용자는 합치려는 이미지를 1개 이상 선택한다.
2. 합쳐진 이미지가 저장될 경로를 지정한다.
3. 가로넓이, 간격, 포맷 옵션을 지정한다.
4. 시작 버튼을 통해 이미지를 합친다.
5. 닫기 버튼을 통해 프로그램을 종료한다.

## [기능 명세]
1. 파일추가 : 리스트 박스에 파일 추가
2. 선택삭제 : 리스트 박스에서 선택된 항목 삭제
3. 찾아보기 : 저장 폴더를 선택하면 텍스트 위젯에 입력
4. 가로넓이 : 이미지 넓이 지정 (원본유지, 1024, 800, 640)
5. 간격 : 이미지 간의 간격 지정 (없음, 좁게, 보통, 넓게)
6. 포맷 : 저장 이미지 포맷 지정 (PNG, JPG, BMP)
7. 시작 : 이미지 합치기 작업 실행
8. 진행상황 : 현재 진행중인 파일 순서에 맞게 반영
9. 닫기 : 프로그램 종료

![alt text](image.png)


# 예제 1) 레이아웃 1 - 파일 목록과 저장 경로 영역
## 목차

1. 프로그램 기본 창 생성
2. 파일 프레임
3. 리스트 프레임
4. 스크롤바와 리스트박스 연결
5. 저장 경로 프레임
6. 창 크기 변경 비활성화

<br>
<details>
<summary>접기/펼치기</summary>
<br>

![alt text](image-1.png)

이미지 병합 프로그램의 첫 번째 레이아웃에서는 파일 추가/삭제 버튼, 파일 목록 리스트박스, 저장 경로 입력 영역을 구성한다.
여러 위젯을 기능별로 나누기 위해 `Frame`과 `LabelFrame`을 사용하고, 파일 목록처럼 스크롤이 필요한 영역은 `Scrollbar`와 `Listbox`를 서로 연결한다.

## 1. 프로그램 기본 창 생성

```py
from tkinter import *

root = Tk()
root.title("Nado GUI")
```

`Tk()`로 프로그램 창을 만들고, `title()`로 창 제목을 지정한다.
이후 생성하는 모든 위젯은 `root` 또는 `root` 안에 배치된 프레임을 부모로 가진다.

## 2. 파일 프레임

```py
# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제")
btn_del_file.pack(side="right")
```

`file_frame`은 파일 관련 버튼을 묶는 영역이다.
버튼의 부모를 `root`가 아니라 `file_frame`으로 지정했기 때문에 두 버튼은 `file_frame` 안에 배치된다.

- `padx`, `pady`: 버튼 내부의 좌우/상하 여백
- `width`: 버튼 너비
- `side="left"`: 위젯을 왼쪽에 배치
- `side="right"`: 위젯을 오른쪽에 배치

`Button`을 생성할 때의 `padx`, `pady`는 버튼 내부 여백이다.
즉, 버튼 글자와 버튼 테두리 사이의 공간을 늘린다.

## 3. 리스트 프레임

```py
# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both")
```

`list_frame`은 파일 목록을 보여줄 `Listbox`와 세로 스크롤바를 함께 담는 영역이다.
스크롤바와 리스트박스를 같은 프레임 안에 넣으면 두 위젯을 나란히 배치하기 쉽다.

`fill="both"`는 위젯이 할당받은 공간의 가로와 세로를 모두 채우도록 한다.
`fill="x"`는 가로, `fill="y"`는 세로, `fill="both"`는 가로와 세로 방향을 의미한다.

## 4. 스크롤바와 리스트박스 연결

```py
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(
    list_frame,
    selectmode="extended",
    height=15,
    yscrollcommand=scrollbar.set
)
list_file.pack(side="left", fill="both", expand=True)

scrollbar.config(command=list_file.yview)
```

`Scrollbar`는 단독으로 사용하는 위젯이 아니라, 스크롤할 대상 위젯과 서로 연결해서 사용한다.
여기서는 `Listbox`와 `Scrollbar`를 연결한다.

### Scrollbar 배치

```py
scrollbar.pack(side="right", fill="y")
```

스크롤바를 `list_frame`의 오른쪽에 배치하고, 할당받은 공간의 세로를 모두 채우도록 한다.
`fill="y"`는 세로 방향으로 늘어나게 하는 옵션이다.

### Listbox 생성

```py
list_file = Listbox(
    list_frame,
    selectmode="extended",
    height=15,
    yscrollcommand=scrollbar.set
)
```

- `selectmode="extended"`: 여러 항목을 동시에 선택할 수 있게 한다.
- `height=15`: 리스트박스에 표시할 높이를 지정한다.
- `yscrollcommand=scrollbar.set`: 리스트박스의 세로 스크롤 위치를 스크롤바에 전달한다.

### Listbox 배치

```py
list_file.pack(side="left", fill="both", expand=True)
```

리스트박스를 `list_frame`의 왼쪽에 배치하고, 가로와 세로 방향으로 영역을 채우도록 한다.

- `fill="both"`: 할당받은 공간의 가로와 세로를 모두 채움
- `expand=True`: 부모 위젯에 남는 공간이 있으면 해당 위젯이 공간을 더 배정받음

`expand=True`는 남는 공간을 배정받게 하는 옵션이고, `fill`은 배정받은 공간 안에서 어느 방향으로 채울지 정하는 옵션이다.

### 스크롤 동작 연결

```py
scrollbar.config(command=list_file.yview)
```

스크롤바를 움직였을 때 리스트박스의 세로 화면이 함께 움직이도록 연결한다.
리스트박스와 스크롤바는 아래처럼 양쪽 연결이 필요하다.

- `yscrollcommand=scrollbar.set`: 리스트박스의 움직임을 스크롤바에 알려줌
- `command=list_file.yview`: 스크롤바의 움직임을 리스트박스에 알려줌

## 5. 저장 경로 프레임

```py
# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack()

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right")
```

`LabelFrame`은 제목이 있는 프레임이다.
여기서는 `text="저장경로"`를 전달하여 저장 경로 입력 영역이라는 제목을 보여준다.

### Entry 위젯

```py
txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)
```

`Entry`는 한 줄짜리 입력 위젯이다.
저장 폴더를 선택하면 나중에 이 입력칸에 경로가 표시되도록 사용할 수 있다.

- `side="left"`: 왼쪽에 배치
- `fill="x"`: 할당받은 공간의 가로를 모두 채움
- `expand=True`: 남는 가로 공간을 배정받음
- `ipady=4`: 위젯 내부의 세로 여백을 추가해서 높이를 키움

`ipady`의 `i`는 internal을 의미한다.
따라서 `ipadx`, `ipady`는 위젯 내부 여백이고, `padx`, `pady`는 보통 위젯 바깥 여백으로 사용된다.

### 찾아보기 버튼

```py
btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right")
```

`찾아보기` 버튼은 저장 폴더를 선택하는 기능과 연결될 버튼이다.
현재 예제에서는 레이아웃만 만들고, 실제 폴더 선택 기능은 이후 단계에서 추가한다.

## 6. 창 크기 변경 비활성화

```py
root.resizable(False, False)
root.mainloop()
```

`resizable(False, False)`는 창의 가로, 세로 크기 변경을 비활성화한다.
`mainloop()`는 프로그램 창이 바로 종료되지 않고 이벤트를 계속 받을 수 있도록 실행 루프를 시작한다.

## 전체 코드

```py
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
list_frame = Frame(root)
list_frame.pack(fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)

scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack()

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right")

root.resizable(False, False)
root.mainloop()
```

</details>
<br>
<hr>
<br>

# 예제 2) 레이아웃 2 - 옵션, 진행상황, 실행 영역
## 목차

1. A) 옵션 프레임
2. B) 파일 프레임 가로 채우기
3. C) 저장 경로 프레임 가로 채우기
4. D) 진행상황 Progressbar
5. E) 실행 프레임
6. 변경 코드 흐름

<br>
<details>
<summary>접기/펼치기</summary>
<br>

![alt text](image-2.png)

첫 번째 레이아웃에서 파일 목록과 저장 경로 영역을 만든 뒤, 두 번째 레이아웃에서는 이미지 병합에 필요한 옵션 영역, 진행상황 표시 영역, 실행 버튼 영역을 추가한다.
옵션 선택에는 `ttk.Combobox`를 사용하고, 진행률 표시는 `ttk.Progressbar`와 `DoubleVar`를 연결해서 구성한다.

## 1. A) 옵션 프레임

```py
import tkinter.ttk as ttk

### 생략

## A) 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack()
```

`ttk.Combobox`를 사용하기 위해 `tkinter.ttk` 모듈을 `ttk`라는 이름으로 가져온다.
`frame_option`은 가로넓이, 간격, 포맷 옵션을 한 줄에 묶어서 배치하는 영역이다.

`LabelFrame`은 일반 `Frame`처럼 위젯을 담을 수 있으면서, `text` 옵션으로 영역 제목을 표시할 수 있다.

### 가로넓이 옵션

```py
## 1. 가로 넓이 옵션
### 1-1. 가로 넓이 라벨
Label(frame_option, text="가로넓이", width=8).pack(side="left")

### 1-2. 가로 넓이 콤보
opt_width=["원본 유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left")
```

`Label`은 옵션 이름을 보여주고, `Combobox`는 사용자가 선택할 수 있는 값을 목록으로 제공한다.

- `state="readonly"`: 사용자가 직접 입력하지 못하고 목록에서만 선택하게 함
- `values=opt_width`: 콤보박스에 표시할 선택 목록
- `current(0)`: 첫 번째 항목을 기본값으로 선택
- `side="left"`: 옵션들을 왼쪽부터 차례대로 배치

### 간격 옵션

```py
## 2. 간격 옵션
### 2-1. 간격 옵션 라벨
Label(frame_option, text="간격", width=8).pack(side="left")

opt_space=["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left")
### 2-2. 간격 옵션 라벨
```

간격 옵션도 같은 방식으로 구성한다.
나중에 이미지 병합 기능을 구현할 때 선택된 값에 따라 이미지 사이 여백을 다르게 적용할 수 있다.

### 파일 포맷 옵션

```py
## 3. 파일 포맷 옵션
Label(frame_option, text="포맷", width=8).pack(side="left")

opt_format=["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left")
```

포맷 옵션은 저장할 이미지 파일 형식을 선택하는 영역이다.
`PNG`, `JPG`, `BMP` 중 하나를 선택하도록 콤보박스를 만든다.

## 2. B) 파일 프레임 가로 채우기

```py
## B) 파일 프레임 가로 채우기
### 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x") # B) x축 기준 간격 펼치기

### 생략
```

기존 파일 프레임에 `fill="x"`를 추가해서 가로 방향으로 부모 영역을 채우도록 한다.
`width`로 고정 너비를 지정하는 대신, 창이나 부모 위젯이 가진 가로 공간에 맞게 자연스럽게 늘어나게 하는 방식이다.

## 3. C) 저장 경로 프레임 가로 채우기

```py
## C) 저장 경로 프레임 가로 채우기
### 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x") # C) 저장경로 x축 기준 간격 펼치기

txt_dest_path = Entry(path_frame, width=50)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4) # iapy: 높이 조정

### 생략
```

저장 경로 영역도 `fill="x"`로 가로 공간을 채운다.
안쪽의 `Entry`에는 `fill="x"`와 `expand=True`를 함께 사용해서, 찾아보기 버튼을 제외한 남은 가로 공간을 입력칸이 차지하도록 한다.

- `fill="x"`: 배정받은 공간의 가로 방향을 채움
- `expand=True`: 부모 위젯에 남는 공간이 있으면 해당 위젯이 더 배정받음
- `width=50`: 입력칸의 기본 요청 너비
- `ipady=4`: 입력칸 내부 세로 여백을 늘려 높이를 조정

## 4. D) 진행상황 Progressbar

```py
### 생략

## D) 진행상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x")

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x")
```

`frame_progress`는 이미지 병합 진행률을 보여주는 영역이다.
`Progressbar`는 `ttk`에서 제공하는 진행 표시 위젯이고, `variable` 옵션에 변수를 연결해서 진행률 값을 관리할 수 있다.

- `DoubleVar()`: 실수 값을 저장할 수 있는 Tkinter 변수
- `maximum=100`: 진행률의 최대값을 100으로 지정
- `variable=p_var`: 진행률 값을 `p_var`와 연결
- `fill="x"`: 진행바가 가로 방향으로 영역을 채우도록 배치

나중에 이미지 병합 작업을 실행하면서 `p_var.set(값)`을 호출하면 진행바가 해당 값에 맞게 갱신된다.

## 5. E) 실행 프레임

```py
### 생략

## E) 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x")

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right")

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12)
btn_start.pack(side="right")

### 생략
```

`frame_run`은 프로그램 실행과 종료 버튼을 담는 영역이다.
두 버튼 모두 `side="right"`로 배치했기 때문에 오른쪽부터 차례대로 붙는다.

`닫기` 버튼에는 `command=root.quit`을 연결해서 버튼을 누르면 Tkinter 이벤트 루프가 종료되도록 한다.
`시작` 버튼은 이후 이미지 병합 기능을 구현할 때 실제 작업 함수와 연결할 수 있다.

## 6. 변경 코드 흐름

```py
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")

## B) 파일 프레임 가로 채우기
### 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x") # B) x축 기준 간격 펼치기

### 생략

## 리스트 프레임
### 생략

## C) 저장 경로 프레임 가로 채우기
### 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x") # C) 저장경로 x축 기준 간격 펼치기

txt_dest_path = Entry(path_frame, width=50)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4) # iapy: 높이 조정

### 생략

## A) 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack()

## 1. 가로 넓이 옵션
### 1-1. 가로 넓이 라벨
Label(frame_option, text="가로넓이", width=8).pack(side="left")
### 1-2. 가로 넓이 콤보
opt_width=["원본 유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left")

## 2. 간격 옵션
### 2-1. 간격 옵션 라벨
Label(frame_option, text="간격", width=8).pack(side="left")
opt_space=["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left")
### 2-2. 간격 옵션 라벨

## 3. 파일 포맷 옵션
Label(frame_option, text="포맷", width=8).pack(side="left")
opt_format=["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left")

## D) 진행상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x")

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x")

## E) 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x")

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right")

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12)
btn_start.pack(side="right")

root.resizable(False, False)
root.mainloop()
```

</details>
<br>
<hr>
<br>

# 예제 3) 레이아웃 3 - 여백과 높이 조정
## 목차

1. A) 간격 띄우기 - `padx`, `pady`
2. B) 프레임 높이 조정 - `ipady`
3. 변경 코드 흐름

<br>
<details>
<summary>접기/펼치기</summary>
<br>

![alt text](image-3.png)

이번 단계에서는 각 영역에 `padx`, `pady`로 바깥 여백을 주고, 일부 프레임에는 `ipady`로 내부 높이를 조정한다.
아래는 어느 영역에 적용했는지 기준으로 정리한 변경 내역이다.

## 1. A) 간격 띄우기 - `padx`, `pady`

`padx`, `pady`는 위젯 바깥 간격을 만든다.
파일/리스트/저장경로/옵션/진행상황/실행 영역에 적용했다.

- 파일/리스트 프레임

```py
### 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # x축 기준 간격 펼치기 / A) 간격 띄우기 - pad

### 생략

### 리스트 프레임
list_frame=Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)
```

- 저장 경로 영역

```py
### 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=4) # 저장경로 x축 기준 간격 펼치기 / B) 프레임 높이 조정 - ipad

txt_dest_path = Entry(path_frame, width=50)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # iapy: 높이 조정 / A) 간격 띄우기 - pad

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right", padx=5, pady=5)
```

- 옵션 영역

```py
### 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=4) # B) 프레임 높이 조정 - ipad

### 가로 넓이 라벨
Label(frame_option, text="가로넓이", width=8).pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad

### 생략

cmb_width.pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad

### 생략

Label(frame_option, text="포맷", width=8).pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad

### 생략

cmb_format.pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad
```

- 진행상황/실행 영역

```py
### 진행상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=4) # B) 프레임 높이 조정 - ipad / B) 프레임 높이 조정 - ipad

### 생략

progress_bar.pack(fill="x", padx=5, pady=5) # A) 간격 띄우기 - pad

### 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

### 생략

btn_close.pack(side="right", padx=5, pady=5) # A) 간격 띄우기 - pad

btn_start.pack(side="right", padx=5, pady=5) # A) 간격 띄우기 - pad
```

## 2. B) 프레임 높이 조정 - `ipady`

`ipady`는 위젯 내부의 세로 여백을 만든다.
저장 경로, 옵션, 진행상황 `LabelFrame`에 적용했다.

- 높이를 조정한 프레임

```py
### 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=4) # 저장경로 x축 기준 간격 펼치기 / B) 프레임 높이 조정 - ipad

### 생략

### 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=4) # B) 프레임 높이 조정 - ipad

### 생략

### 진행상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=4) # B) 프레임 높이 조정 - ipad / B) 프레임 높이 조정 - ipad
```

## 3. 변경 코드 흐름

```py
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")

## A) 파일 프레임 간격 띄우기
### 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # x축 기준 간격 펼치기 / A) 간격 띄우기 - pad

### 생략

## A) 리스트 프레임 간격 띄우기
### 리스트 프레임
list_frame=Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

### 생략

## B) 저장 경로 프레임 높이 조정
### 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=4) # 저장경로 x축 기준 간격 펼치기 / B) 프레임 높이 조정 - ipad

## A) 저장 경로 내부 위젯 간격 띄우기
txt_dest_path = Entry(path_frame, width=50)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # iapy: 높이 조정 / A) 간격 띄우기 - pad

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right", padx=5, pady=5)

### 생략

## B) 옵션 프레임 높이 조정
### 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=4) # B) 프레임 높이 조정 - ipad

## A) 옵션 위젯 간격 띄우기
### 가로 넓이 라벨
Label(frame_option, text="가로넓이", width=8).pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad

### 생략

cmb_width.pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad

### 생략

Label(frame_option, text="포맷", width=8).pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad

### 생략

cmb_format.pack(side="left", padx=5, pady=5) # A) 간격 띄우기 - pad

## B) 진행상황 프레임 높이 조정
### 진행상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=4) # B) 프레임 높이 조정 - ipad / B) 프레임 높이 조정 - ipad

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5) # A) 간격 띄우기 - pad

## A) 실행 프레임과 버튼 간격 띄우기
### 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

### 생략

btn_close.pack(side="right", padx=5, pady=5) # A) 간격 띄우기 - pad

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12)
btn_start.pack(side="right", padx=5, pady=5) # A) 간격 띄우기 - pad

root.resizable(False, False)
root.mainloop()
```

</details>
<br>
<hr>
<br>

# 예제 4) 기본 기능 1 - 파일 추가와 선택 삭제
## 목차

1. A) 파일 추가
2. B) 선택 삭제
3. 변경 코드 흐름

<br>
<details>
<summary>접기/펼치기</summary>
<br>

파일 목록 영역에 실제 동작을 연결하는 단계이다.
함수는 파일 프레임을 만든 뒤, 버튼을 생성하기 전에 정의한다.

## 1. A) 파일 추가

`filedialog.askopenfilenames()`는 여러 파일을 한 번에 선택할 수 있는 파일 선택 창을 띄운다.
`title`은 파일 선택 창 제목, `filetypes`는 선택 가능한 파일 형식, `initialdir`은 처음 열릴 기본 경로를 의미한다.
선택된 파일 경로들은 `Listbox`의 마지막 위치에 순서대로 추가한다.

- 적용한 영역

```py
# 생략
from tkinter import filedialog
# 생략

# 생략(파일 프레임)
def add_file():
  files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
                                      filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")),
                                      initialdir="C:/"
  )

  for file in files:
    list_file.insert(END, file)

# 생략(선택 삭제 함수)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")
# 생략(선택 삭제 버튼 정의 및 출력)
```

## 2. B) 선택 삭제

`list_file.curselection()`은 현재 선택된 항목들의 인덱스를 반환한다.
여러 항목을 앞에서부터 삭제하면 뒤 항목의 인덱스가 앞으로 당겨져 삭제 대상이 어긋날 수 있다.
그래서 `reversed()`로 선택 인덱스를 뒤에서부터 순회한다.
현재 코드에서는 삭제되는 인덱스를 `print(index)`로 확인하고, 이어서 `list_file.delete(index)`로 리스트박스에서 해당 항목을 제거한다.

- 적용한 영역

```py
def add_file():
  # 생략(파일 추가)

def del_file():
  for index in reversed(list_file.curselection()):
    print(index)
    list_file.delete(index)

# 생략(파일 추가 버튼 배치)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")
```

## 3. 변경 코드 흐름

```py
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")

# 생략(파일 프레임)

file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

# 생략(파일 추가/선택 삭제 버튼 기능 정의)

def add_file():
  files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
                                      filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")),
                                      initialdir="C:/"
  )

  for file in files:
    list_file.insert(END, file)

def del_file():
  for index in reversed(list_file.curselection()):
    print(index)
    list_file.delete(index)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")

# 생략(리스트 프레임 이하 레이아웃)

root.resizable(False, False)
root.mainloop()
```

</details>
<br>
<hr>
<br>

# 예제 5) 기본 기능 2 - 저장 경로와 시작 검증
## 목차

1. C) 저장 경로 선택
2. D) 시작 전 옵션/입력값 확인
3. 변경 코드 흐름


<br>
<details>
<summary>접기/펼치기</summary>
<br>

저장 경로 선택 버튼과 시작 버튼에 실제 동작을 연결하는 단계이다.
저장 경로는 폴더 선택 창에서 받아와 `Entry`에 표시하고, 시작 버튼은 파일 목록과 저장 경로가 비어 있는지 먼저 확인한다.

## 1. C) 저장 경로 선택

`filedialog.askdirectory()`는 폴더 선택 창을 띄우고, 선택한 폴더 경로를 반환한다.
폴더 선택을 취소하면 함수 실행을 중단하고, 정상적으로 선택한 경우에는 기존 입력값을 지운 뒤 새 경로를 넣는다.

- 적용한 영역

```py
# 생략
from tkinter import filedialog
# 생략

def browse_dest_path():
  folder_selected = filedialog.askdirectory()
  if folder_selected == None:
    return

  txt_dest_path.delete(0, END)
  txt_dest_path.insert(0, folder_selected)

# 생략(시작 함수)

path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=4)

txt_dest_path = Entry(path_frame, width=50)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)
```

## 2. D) 시작 전 옵션/입력값 확인

시작 버튼을 누르면 콤보박스에서 선택된 옵션 값을 확인한다.
파일 목록이 비어 있거나 저장 경로가 비어 있으면 `messagebox.showwarning()`으로 경고창을 띄우고 작업을 중단한다.

- 적용한 영역

```py
# 생략
import tkinter.messagebox as msgbox

# 생략(저장 경로 함수)

def start():
  print("가로넓이 : ", cmb_width.get())
  print("간격 : ", cmb_space.get())
  print("포맷 : ", cmb_format.get())

  if list_file.size() == 0:
    msgbox.showwarning("경고", "이미지 파일을 추가하세요")
    return

  if len(txt_dest_path.get()) == 0:
    msgbox.showwarning("경고", "저장 경로를 선택하세요")
    return

# 생략(실행 프레임)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)
```

## 3. 변경 코드 흐름

```py
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

root = Tk()
root.title("Nado GUI")

def browse_dest_path():
  folder_selected = filedialog.askdirectory()
  if folder_selected == None:
    return

  txt_dest_path.delete(0, END)
  txt_dest_path.insert(0, folder_selected)

def start():
  print("가로넓이 : ", cmb_width.get())
  print("간격 : ", cmb_space.get())
  print("포맷 : ", cmb_format.get())

  if list_file.size() == 0:
    msgbox.showwarning("경고", "이미지 파일을 추가하세요")
    return

  if len(txt_dest_path.get()) == 0:
    msgbox.showwarning("경고", "저장 경로를 선택하세요")
    return

# 생략(파일/리스트 프레임)

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 생략(옵션/진행상황/실행 프레임)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()
```

</details>
<br>
<hr>
<br>

# 예제 ) 
## 목차



<br>
<details>
<summary>접기/펼치기</summary>
<br>


</details>
<br>
<hr>
<br>
