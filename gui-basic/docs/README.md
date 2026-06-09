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