import tkinter as tk

def open_setting_window():
    popup.title("환경설정")
    popup.geometry("300x150")
    
    popup.geometry(f"+{root.winfo_x() + 50}+{root.winfo_y() + 50}")
    
    popup.grab_set()

    lbl = tk.Label(popup, text="새로운 사용자 이름을 입력하세요:")
    lbl.pack(pady=10)
    
    entry = tk.Entry(popup, width=20)
    entry.pack(pady=5)
    entry.insert(0, main_label["text"])

    def apply_and_close():
        new_name = entry.get()
        main_label.config(text=new_name)
        popup.destroy()  

    btn_save = tk.Button(popup, text="저장 및 닫기", command=apply_and_close)
    btn_save.pack(pady=10)


root = tk.Tk()
root.title("메인 프로그램")
root.geometry("400x200")

main_label = tk.Label(root, text="기존 사용자", font=("Arial", 16, "bold"))
main_label.pack(pady=30)

btn_open = tk.Button(root, text="이름 변경하기 (팝업창 열기)", command=open_setting_window, bg="lightblue")
btn_open.pack(pady=10)

root.mainloop()