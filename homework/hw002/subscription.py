class Subscription:
    def __init__(self):
        self.sub_list = []

    def add_register(self):
        print("\n--- 구독 서비스 등록 ---")
        name = input("서비스명을 입력해주세요.: ")
        
        while True:
            try:
                price = int(input("월 결제 금액을 입력하세요.: "))
                if price < 0:
                    print("금액은 0원 이상이어야 합니다. 다시 입력해주세요.")
                    continue
                break
            except ValueError:
                print("숫자로만 입력해주세요.")

        while True:
            try:
                day = int(input("결제일을 입력하세요 (1~31): "))
                if 1 <= day <= 31:
                    break
                print("결제일은 1부터 31 사이만 입력 가능합니다.")
            except ValueError:
                print("숫자로만 입력해주세요.")

        category = input("카테고리를 입력해주세요. (예: OTT, 배달): ")
        
        self.sub_list.append([name, price, day, category])
        print(f"[{name}] 등록이 완료되었습니다.")

if __name__ == "__main__":
    mysub = Subscription()
    
    while True:
        print("\n--- [메뉴] ---")
        try:
            user_choice = int(input("원하시는 기능을 선택해주세요.\n 1. 구독 등록 \n 0. 종료\n >>> "))
            
            if user_choice == 1:
                mysub.add_register()
                print("\n현재 저장된 리스트:", mysub.sub_list)
            elif user_choice == 0:
                print("프로그램을 종료합니다.")
                break
            else:
                print("1번 또는 0번만 선택해주세요.")
                
        except ValueError:
            print("숫자로만 입력해주세요.")