import os
from modules.health_db import HealthDB
from modules.health_logic import HealthManager


def print_records(records):
    if not records:
        print("조회된 건강정보가 없습니다.")
        return
    print("-" * 78)
    print(f"{'ID':<12} {'이름':<10} {'생년':<6} {'성별':<4} {'키(cm)':<8} {'몸무게(kg)':<10} {'BMI':<7} {'판정'}")
    print("-" * 78)
    for r in records:
        print(
            f"{r.id:<12} {r.name:<10} {str(r.birth_year):<6} {r.gender:<4} "
            f"{r.height:<8} {r.weight:<10} {r.bmi:<7} {r.status}"
        )
    print("-" * 78)


def menu_add(manager: HealthManager):
    print("\n[건강정보 추가]")
    name = input("이름: ").strip()
    try:
        birth_year = int(input("생년(예: 2004): ").strip())
        height = float(input("키(cm): ").strip())
        weight = float(input("몸무게(kg): ").strip())
    except ValueError:
        print("생년은 정수, 키와 몸무게는 숫자로 입력해야 합니다.")
        return
    gender = input("성별(남/여): ").strip()

    ok, msg, _ = manager.add_record(name, birth_year, gender, height, weight)
    print(msg)


def menu_list(manager: HealthManager):
    print("\n[건강정보 목록 조회]")
    records = manager.get_all_records()
    print_records(records)


def menu_search_detail(manager: HealthManager):
    print("\n[검색 및 상세조회]")
    keyword = input("검색어(식별번호, 이름, 생년, 비만도 등): ").strip()
    matched = manager.search_records(keyword)
    print_records(matched)

    if matched:
        detail_id = input("상세조회할 식별번호 입력(엔터 시 건너뜀): ").strip()
        if detail_id:
            rec = manager.get_record_by_id(detail_id)
            if rec:
                print("=== 상세 정보 ===")
                print(f"식별번호 : {rec.id}")
                print(f"이름     : {rec.name}")
                print(f"생년     : {rec.birth_year}")
                print(f"성별     : {rec.gender}")
                print(f"키       : {rec.height} cm")
                print(f"몸무게   : {rec.weight} kg")
                print(f"BMI      : {rec.bmi}")
                print(f"비만판정 : {rec.status}")
            else:
                print("해당 식별번호를 찾을 수 없습니다.")


def menu_update_or_delete(manager: HealthManager):
    print("\n[수정 및 삭제]")
    record_id = input("대상 식별번호 입력: ").strip()
    rec = manager.get_record_by_id(record_id)
    if rec is None:
        print("해당 식별번호의 데이터가 없습니다.")
        return

    print(f"선택됨 -> ID: {rec.id}, 이름: {rec.name}, 생년: {rec.birth_year}, 성별: {rec.gender}, 키: {rec.height}, 몸무게: {rec.weight}, BMI: {rec.bmi}({rec.status})")
    action = input("1. 수정 / 2. 삭제 / 0. 취소 : ").strip()

    if action == "1":
        name_in = input(f"새 이름(현재: {rec.name}, 엔터 시 유지): ").strip()
        birth_in = input(f"새 생년(현재: {rec.birth_year}, 엔터 시 유지): ").strip()
        gender_in = input(f"새 성별(현재: {rec.gender}, 엔터 시 유지): ").strip()
        height_in = input(f"새 키(cm)(현재: {rec.height}, 엔터 시 유지): ").strip()
        weight_in = input(f"새 몸무게(kg)(현재: {rec.weight}, 엔터 시 유지): ").strip()

        try:
            new_name = name_in if name_in else None
            new_birth = int(birth_in) if birth_in else None
            new_gender = gender_in if gender_in else None
            new_height = float(height_in) if height_in else None
            new_weight = float(weight_in) if weight_in else None
        except ValueError:
            print("숫자 입력 형식이 올바르지 않습니다.")
            return

        ok, msg, _ = manager.update_record(
            record_id=rec.id,
            name=new_name,
            birth_year=new_birth,
            gender=new_gender,
            height=new_height,
            weight=new_weight,
        )
        print(msg)

    elif action == "2":
        confirm = input(f"정말 {rec.id}({rec.name}) 데이터를 삭제할까요? (y/n): ").strip().lower()
        if confirm == "y":
            ok, msg = manager.delete_record(rec.id)
            print(msg)
        else:
            print("삭제를 취소했습니다.")


def menu_statistics(manager: HealthManager):
    print("\n[통계조회]")
    stats = manager.get_statistics()
    print(f"총 레코드 수 : {stats['count']}명")
    print(f"키 평균/표준편차    : {stats['height_mean']} cm / {stats['height_std']}")
    print(f"몸무게 평균/표준편차  : {stats['weight_mean']} kg / {stats['weight_std']}")
    print(f"BMI 평균/표준편차     : {stats['bmi_mean']} / {stats['bmi_std']}")
    print("비만도 분포         :", stats["status_counts"])


def menu_load(manager: HealthManager):
    print("\n[파일에서 가져오기]")
    ftype = input("파일 형식(json / csv / txt / pkl) [기본: json]: ").strip().lower() or "json"
    default_path = os.path.join("data", f"health_data.{ftype}")
    path_in = input(f"파일 경로(기본: {default_path}): ").strip()
    filepath = path_in if path_in else default_path

    ok, msg, total = manager.load_from_file(filepath, ftype)
    print(f"{msg} (현재 메모리 데이터 수: {total})")


def menu_save(manager: HealthManager):
    print("\n[파일로 저장]")
    ftype = input("저장 형식(json / csv / txt / pkl) [기본: json]: ").strip().lower() or "json"
    default_path = os.path.join("data", f"health_data.{ftype}")
    path_in = input(f"저장 경로(기본: {default_path}): ").strip()
    filepath = path_in if path_in else default_path

    ok, msg = manager.save_to_file(filepath, ftype)
    print(msg)


def main():
    db = HealthDB()
    manager = HealthManager(db)

    default_json = os.path.join("data", "health_data.json")
    if os.path.exists(default_json):
        manager.load_from_file(default_json, "json")

    while True:
        print("\n---------------- 건강정보 관리 시스템 ------")
        print("1. 추가")
        print("2. 목록 조회")
        print("3. 검색 및 상세조회")
        print("4. 수정 및 삭제")
        print("5. 통계조회")
        print("6. 파일에서 가져오기 (모듈1)")
        print("7. 파일로 저장 (모듈1)")
        print("0. 종료")
        print("--------------------------------------------")

        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            menu_add(manager)
        elif choice == "2":
            menu_list(manager)
        elif choice == "3":
            menu_search_detail(manager)
        elif choice == "4":
            menu_update_or_delete(manager)
        elif choice == "5":
            menu_statistics(manager)
        elif choice == "6":
            menu_load(manager)
        elif choice == "7":
            menu_save(manager)
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴 번호를 선택해 주세요.")


if __name__ == "__main__":
    main()