import tkinter as tk

root = tk.Tk()
root.title("Canvas 위젯 활용 예제")
root.geometry("600x500")

canvas = tk.Canvas(root, bg="white", bd=1, relief="solid")
canvas.pack(fill="both", expand=True, padx=10, pady=10)



canvas.create_line(20, 20, 200, 20, fill="blue", width=3)

canvas.create_rectangle(20, 50, 150, 120, fill="lightgray", outline="black", width=2)

canvas.create_oval(180, 50, 250, 120, fill="orange", outline="red")

canvas.create_polygon(300, 20, 350, 100, 250, 100, fill="lightgreen", outline="green")

canvas.create_text(450, 60, text="Canvas 도화지 영역", font=("Arial", 14, "bold"), fill="purple")


def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill="black", outline="black")

canvas.bind("<B1-Motion>", draw)


def clear_canvas():
    canvas.delete("all")

btn_clear = tk.Button(root, text="화면 지우기", command=clear_canvas, bg="lightcoral", fg="white")
btn_clear.pack(pady=(0, 10))

root.mainloop()