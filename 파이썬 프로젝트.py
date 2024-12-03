from tkinter import *
import random
import os
from PIL import Image, ImageTk

# 윈도우 설정
window = Tk()
window.title("티니핑 맞추기")
window.option_add("*Font", "SUIT 16")

Label(window, text="                              티니핑을 맞춰보자!").grid(row=0, column=0)

# 이미지 파일 경로 설정
path = r"C:\Users\a0102\OneDrive\바탕 화면\파이썬 프로젝트 티니핑 맞추기"
os.chdir(path)  # 해당 폴더로 이동
files = os.listdir(path)

word = random.choice(files)  # 랜덤으로 정답 선택
jpg_img = []  # 이미지 저장할 리스트
ci = []  # 이미지 파일명 저장할 리스트
f = None  # 이미지 객체

# 정답 이미지 표시
def 새문제():
    global word, f, image, result

    word = random.choice(files)  # 랜덤으로 정답을 새로 선택
    print(f"정답: {os.path.splitext(word)[0]}")  # 콘솔에 정답 출력

    # 기존 이미지 삭제
    if 'label_image' in globals():
        image.grid_forget()

    # 이미지 새로 로드
    f = Image.open(word)
    photo = ImageTk.PhotoImage(f)
    image = Label(window, image=photo)
    image.image = photo
    image.grid(row=5, column=0, columnspan=2, rowspan=2)

    # 결과 레이블 초기화
    result.config(text="")

# 검색 값 처리
def get_search_value():
    search_value = entry.get()  # Entry에서 값 가져오기
    print(f"답: {search_value}")  # 콘솔에 답 출력

    # 정답 비교
    if search_value == os.path.splitext(word)[0]:  # 정답 비교
        result.config(text="정답입니다! 🎉")
        entry.delete(0, END)  # 정답을 맞히면 입력창 초기화
        # 새로운 문제를 보여줌
        새문제()
    else:
        result.config(text="틀렸습니다. 다시 시도해 보세요.")

# 검색창
entry = Entry(window, width=30)
entry.grid(row=10, column=0)

# 검색 버튼
button = Button(window, text="확인", width=10, command=get_search_value)
button.grid(row=10, column=1)

# 엔터 키로 확인
window.bind('<Return>', lambda event: get_search_value())

# 결과 레이블
result = Label(window, text="")
result.grid(row=11, column=0, columnspan=2)

# 최초 문제 로드
새문제()

# 메인 루프 실행
window.mainloop()