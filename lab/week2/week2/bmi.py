def get_bmi(weight_kg: float, height_cm: float) -> float:
    bmi = weight_kg / (height_cm / 100) ** 2
    return bmi

def test_get_bmi():
    height = 170
    weight = 85
    b = get_bmi(weight, height)
    print(f"키({height}) 몸무게({weight})의 bmi는 {b}입니다.")

if __name__ == "__main__":
    test_get_bmi()
