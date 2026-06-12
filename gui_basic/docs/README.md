# [루트/README.md](../../README.md)

# 예제 1) 프레임

## 목차

1. 프로그램 초기화
2. 프로그램 창 타이틀  
3. 프로그램 창 크기 설정 및 위치 지정
4. 프로그램 loop 실행

<br>
<details>
<summary>접기/펼치기</summary>
<br>


Tkinter 라이브러리는 Python을 설치할 때 자동으로 모듈이 포함되기 때문에 따로 설치하거나 환경설정을 할 필요가 없다.  

## tkinter 최소 실행
![alt text](image.png)
```py
from tkinter import *

root = Tk()
root.mainloop()
```
1. from ~ import 구문을 활용하여 tkinter 패키지 전체 import.  
2. Tk 클래스 인스턴스 생성 및 할당
3. 프로그램 이벤트 루프 호출  

### 이벤트 루프 역할
- 프로그램 창이 종료되지 않도록 유지
- 마우스, 키보드 입력 감지
- 버튼 클릭, 창 닫기 등의 이벤트 감지 및 처리

## 프레임 레이아웃 기본 설정
- `title(string: str)` : 창 타이틀 지정
- `geometry(newGeometry: str)`: 창 크기설정  
  "{width}x{height}" 형태의 텍스트 문자열로 설정
- `resizable(width: bool,height: bool)`: 프로그램 창 크기 변경 비활성  
  bool 타입의 매개변수로 너비, 높이를 각각 비활성화

```py
from tkinter import *

root = Tk()
root.title("Nado GUI") # 프로그램 창 타이틀
root.geometry("640x480") # 프로그램 창 크기 설정 (가로x세로)
root.geometry("640x480+300+100") # 프로그램 창 크기 설정 및 위치 지정 (가로 * 세로 + X좌표 Y좌표)
root.resizable(False, False) # 프로그램 창 크기 변경 비활성 (너비, 높이)
root.mainloop()
```


</details>
<br>
<hr>
<br>

# 예제 2) 버튼 위젯

위젯이란 버튼이나 체크박스나 혹은 글자를 입력할 수 있는 텍스트상자 같은 것들을 말한다.  

## 목차
A) 버튼 인스턴스 생성.  
  1. 텍스트 타입 버튼 정의
  2. 버튼 크기 조정
      - 버튼 내부 좌우 여백(픽셀) : padx, pady
      - 너비/높이 : width, height
  3. 버튼 색상 조정
  4. 이미지 타입 버튼
  5. 버튼 동작 - 함수 정의 및 연동
B) 버튼 배치


<br>
<details>
<summary>접기/펼치기</summary>
<br>

![alt text](image-1.png)

## A/B)기본 버튼 출력

버튼을 구성하기 위해서는 먼저 버튼 클래스를 통해 버튼 인스턴스를 생성하고, 해당 인스턴스로 부터 pack() 함수를 호출하여 최종적으로 버튼을 배치해야 출력된다.  
출력될 타입은 대표적으로 text 타입과 image 타입이 있다.  
먼저 아래와 같이 기본 텍스트 타입으로 버튼을 정의하고, 출력해보도록 한다.  
### 1. 텍스트 타입 버튼 정의
  ```py
  # 생략
  btn = Button(root, text="버튼")
  btn.pack()
  # 생략
  ```

### 2. 버튼 크기 조정
버튼 크기는 픽셀단위로 버튼 내부에서 좌우 여백을 지정하는 padx, pady 방식과,  
일반적인 너비, 높이를 지정하는 width, height 방식이 있다.  
- padx, pady: 버튼 내부 내용물 기준으로 버튼까지의 여백을 말하며, padx는 좌우여백, pady는 상하여백을 가리킨다.  
  ```py
  # 생략
  btn = Button(root, padx=5, pady=10, text="버튼")
  btn.pack()
  # 생략
  ```
  여백의 크기이므로, 버튼 내용물의 크기가 커질수록 버튼 크기는 동적으로 변경된다.  
- width, height
  ```py
  # 생략
  btn = Button(root, width=10, height=3, text="버튼")
  btn.pack()
  # 생략
  ```
  padx,pady와는 다르게 width, hegiht는 고정 크기이므로, 버튼 내용물이 커지면, 내용물이 잘려서 출력된다.  
  ```py
  btn = Button(root, width=10, height=3, text="버튼44444444444444444444444")
  btn.pack()
  ```

### 3. 버튼 색상 조정
버튼 색상의 fg는 foreground의 약자로, 글자색을. bg는 background의 약자로 배경색을 의미한다.
Button 인스턴스 생성시 매개변수로 전달하며 영문 텍스트로 색상을 정의한다.
```py
# 생략
btn = Button(root, fg="red", bg="yellow", text="버튼5")
btn.pack()
# 생략
```

### 4. 이미지 타입 버튼
PhotoImnage 클래스의 file 키워드에 이미지 경로를 전달하여 PhotoImange 인스턴스를 생성한 후,   
Button 클래스의 image 키워드에 해당 인스턴스를 전달하여 Button 인스턴스를 생성한다.  
```py
# 생략
photo = PhotoImage(file="gui_basic/img/check.png")
btn = Button(root, image=photo)
btn.pack()
# 생략
```

### 5. 버튼 동작 - 함수 정의 및 연동
일반적인 함수를 정의한 후, Button 클래스의 command 키워드에 해당 함수를 전달하여 Button 인스턴스를 생성한다.  
```py
# 생략
def btncmd():
  print("버튼이 클릭되었어요")
btn = Button(root, text="동작하는 버튼", command=btncmd)
btn.pack()
# 생략
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