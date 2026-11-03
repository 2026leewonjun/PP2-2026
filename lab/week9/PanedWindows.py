import tkinter as tk

root = tk.Tk()
root.title("PanedWindow 크기 조절 예제")
root.geometry("600x400")

# 1. 메인 가로 분할 페인 생성 (좌측 트리메뉴 / 우측 본문 영역 분할용)
# sashrelief="raised"는 구분선을 입체감 있게 보여주며, sashwidth=4는 선 두께를 지정합니다.
main_pane = tk.PanedWindow(root, orient="horizontal", sashrelief="raised", sashwidth=4)
main_pane.pack(fill="both", expand=True)

# --- [좌측 영역] ---
# 가로 분할 페인의 첫 번째 자식으로 프레임을 넣습니다.
left_frame = tk.Frame(main_pane, bg="#E0E0E0")
# minsize는 Frame이 아니라 add()의 옵션입니다. 지정하면 그 이하로 줄일 수 없습니다.
main_pane.add(left_frame, width=150, minsize=100)

left_lbl = tk.Label(left_frame, text="[좌측 메뉴 영역]\n\n여기를 마우스로\n잡고 조절해 보세요.", bg="#E0E0E0")
left_lbl.pack(pady=50, padx=10)


# --- [우측 영역] ---
# 우측 영역은 다시 내부에서 위아래(세로)로 쪼개기 위해 새로운 PanedWindow를 생성합니다.
sub_pane = tk.PanedWindow(main_pane, orient="vertical", sashrelief="raised", sashwidth=4)
main_pane.add(sub_pane) # 메인 가로 페인의 두 번째 자식으로 추가

# [우측 - 상단 영역]
right_top = tk.Frame(sub_pane, bg="#FFFFFF")
sub_pane.add(right_top, height=200, minsize=50)

top_lbl = tk.Label(right_top, text="[우측 상단 본문 영역]", bg="#FFFFFF", font=("Arial", 12, "bold"))
top_lbl.pack(pady=20)

# [우측 - 하단 영역]
right_bottom = tk.Frame(sub_pane, bg="#F0F0F0")
sub_pane.add(right_bottom, height=200, minsize=50)

bottom_lbl = tk.Label(right_bottom, text="[우측 하단 로그/출력 영역]\n상단과 하단의 경계선도 마우스로 조절 가능합니다.", bg="#F0F0F0")
bottom_lbl.pack(pady=20)


root.mainloop()