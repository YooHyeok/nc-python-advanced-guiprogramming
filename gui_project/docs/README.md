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
