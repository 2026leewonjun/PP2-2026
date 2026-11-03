import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Notebook 탭 제어 예제")
root.geometry("450x300")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="기본 설정")
lbl1 = ttk.Label(tab1, text="사용자 계정 정보", font=("Arial", 12, "bold"))
lbl1.pack(pady=15)

entry_name = ttk.Entry(tab1, width=25)
entry_name.insert(0, "닉네임을 입력하세요")
entry_name.pack(pady=5)


tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="알림 설정")

lbl2 = ttk.Label(tab2, text="푸시 알림 수신 동의", font=("Arial", 12, "bold"))
lbl2.pack(pady=15)

chk_email = ttk.Checkbutton(tab2, text="이메일 알림 받기")
chk_sms = ttk.Checkbutton(tab2, text="SMS 문자 알림 받기")
chk_email.pack(anchor="w", padx=40, pady=2)
chk_sms.pack(anchor="w", padx=40, pady=2)


tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="정보 (Info)")

lbl3 = ttk.Label(tab3, text="Tkinter Notebook 버전 1.0\n\nDeveloped by Google LLM", justify="center")
lbl3.pack(pady=50)


def go_to_alarm_tab():
    notebook.select(1)

btn_jump = ttk.Button(root, text="알림 설정 탭으로 바로가기", command=go_to_alarm_tab)
btn_jump.pack(pady=(0, 10))

root.mainloop()