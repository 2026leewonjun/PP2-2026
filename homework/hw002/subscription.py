class Subscription:
    def __init__(self, name, price, day):
        self.name = name
        self.price = price
        self.day = day    

sub_list = []

def register_subscription():
    print("\n--- 구독 서비스 등록 ---")
    
    name = input("서비스명을 입력하세요: ")
    price = int(input("월 결제 금액을 입력하세요: "))
    day = int(input("결제일을 입력하세요: "))

    new_sub = Subscription(name, price, day)
    
    sub_list.append(new_sub)
    
    print(f"[{name}] 등록이 완료되었습니다!")

if __name__ == "__main__":
    register_subscription()