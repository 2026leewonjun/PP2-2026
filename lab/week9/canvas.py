import tkinter as tk

root = tk.Tk()
root.title("Canvas 위젯 활용 예제")
root.geometry("600x500")

# 1. 캔버스 컨테이너 생성 (배경은 흰색, 테두리 두께 1, 회색 테두리 지정)
canvas = tk.Canvas(root, bg="white", bd=1, relief="solid")
# 상단과 좌우를 꽉 채우고 아래쪽에 버튼이 들어갈 공간을 남김
canvas.pack(fill="both", expand=True, padx=10, pady=10)



# [선 그리기] 좌표: (x1, y1) -> (x2, y2), 색상: 파란색, 두께: 3px
canvas.create_line(20, 20, 200, 20, fill="blue", width=3)

# [사각형 그리기] 좌상단 좌표(x1, y1)와 우하단 좌표(x2, y2) 지정, 내부 채우기, 테두리 색상
canvas.create_rectangle(20, 50, 150, 120, fill="lightgray", outline="black", width=2)

# [원 / 타원 그리기] 사각형 가상의 바운딩 박스 안에 외접하는 원을 그림
canvas.create_oval(180, 50, 250, 120, fill="orange", outline="red")

# [다각형 그리기] 꼭짓점 좌표들을 순서대로 나열 (x1, y1, x2, y2, x3, y3...)
canvas.create_polygon(300, 20, 350, 100, 250, 100, fill="lightgreen", outline="green")

# [글자 쓰기] 특정 좌표(x, y)를 중심으로 텍스트 배치
canvas.create_text(450, 60, text="Canvas 도화지 영역", font=("Arial", 14, "bold"), fill="purple")


# 마우스 왼쪽 버튼을 누른 채 움직일 때(B1-Motion) 실행될 함수
def draw(event):
    # event.x와 event.y는 현재 마우스 포인터의 좌표입니다.
    # 아주 작은 원들을 연속해서 그려서 선처럼 보이게 만듭니다.
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill="black", outline="black")

# 캔버스에 마우스 드래그 이벤트 바인딩
canvas.bind("<B1-Motion>", draw)


def clear_canvas():
    canvas.delete("all")  # 캔버스에 그려진 모든 객체를 지웁니다.

btn_clear = tk.Button(root, text="화면 지우기", command=clear_canvas, bg="lightcoral", fg="white")
btn_clear.pack(pady=(0, 10))

root.mainloop()