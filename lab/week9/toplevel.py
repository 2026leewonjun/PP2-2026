import tkinter as tk

# --- 팝업창(Toplevel)을 띄우는 함수 ---
def open_setting_window():
    # 1. 새 창 생성 (root를 부모로 지정)
    popup = tk.Toplevel(root)
    popup.title("환경설정")
    popup.geometry("300x150")
    
    # [옵션] 메인 창의 정중앙 근처에 뜨도록 좌표 설정
    popup.geometry(f"+{root.winfo_x() + 50}+{root.winfo_y() + 50}")
    
    # [옵션] 팝업창이 닫히기 전까지 메인 창을 클릭하지 못하게 독점 (Modal 효과)
    popup.grab_set()

    # 2. 팝업창 내부 위젯 배치
    lbl = tk.Label(popup, text="새로운 사용자 이름을 입력하세요:")
    lbl.pack(pady=10)
    
    entry = tk.Entry(popup, width=20)
    entry.pack(pady=5)
    entry.insert(0, main_label["text"])  # 현재 메인창 이름을 기본값으로 세팅

    # 3. 데이터 적용 및 창 닫기 함수
    def apply_and_close():
        new_name = entry.get()
        main_label.config(text=new_name)  # 메인 창의 라벨 변경
        popup.destroy()                   # 팝업 창 제거

    btn_save = tk.Button(popup, text="저장 및 닫기", command=apply_and_close)
    btn_save.pack(pady=10)


# --- 메인 윈도우(Root) 설정 ---
root = tk.Tk()
root.title("메인 프로그램")
root.geometry("400x200")

# 메인 창 위젯
main_label = tk.Label(root, text="기존 사용자", font=("Arial", 16, "bold"))
main_label.pack(pady=30)

# 버튼을 누르면 open_setting_window 함수가 실행되면서 Toplevel 창이 뜸
btn_open = tk.Button(root, text="이름 변경하기 (팝업창 열기)", command=open_setting_window, bg="lightblue")
btn_open.pack(pady=10)

root.mainloop()