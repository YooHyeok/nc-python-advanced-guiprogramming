# zip()과 unpacking

kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

# zip() : 동일한 index요소 끼리 그룹으로 묶어 튜플형태로 병합한 뒤, 리스트로 반환하는 함수
merged = list(zip(kor, eng)) # 리스트 병합(index 그룹)
print("merged = ", merged) # → [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

# zip() - unpacking : 병합된 그룹 앞의 '*' 연산자로 구조를 해체(unpacking)한 뒤, 원래의 데이터 군집별 튜플로 각각 분리하는 기능
kor2, eng2 = zip(*merged)
print("kor2 = ", kor2) # → ('사과', '바나나', '오렌지')
print("eng2 = ", eng2) # → ('apple', 'banana', 'orange')
