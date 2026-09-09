def say_happy_birthday(name:str) -> None:
    print("안녕하세요")
    print(name + "님의 생일을 축하합니다")
    return None

def test_happy_birthday() :
    say_happy_birthday("원준")
    say_happy_birthday("민석")
    say_happy_birthday("윤성")
    say_happy_birthday("강훈")

def test_happy_birthday2() :
    names = ["원준", "민석", "윤성", "강훈"]
    for name in names:
        say_happy_birthday(name)

def test_happy_birthday3() :
    say_happy_birthday(3.14159)
    say_happy_birthday(100)
    say_happy_birthday([1, 2, 3])


if __name__ == "__main__":
#    test_happy_birthday()
#    test_happy_birthday2()
     test_happy_birthday3()