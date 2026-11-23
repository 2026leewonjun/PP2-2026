from modules.health_db import HealthDB, HealthRecord

class HealthLogic:
    def __init__(self):
        self.db = HealthDB()

    def calculate_bmi(self, height: float, weight: float) -> tuple:
        if height <= 0 or weight <= 0:
            return 0.0, "입력 오류"
        
        height_m = height / 100.0
        bmi = round(weight / (height_m ** 2), 2)
        
        if bmi < 18.5:
            status = "저체중"
        elif bmi < 23.0:
            status = "정상"
        elif bmi < 25.0:
            status = "과체중"
        else:
            status = "비만"
            
        return bmi, status

    def add_health_record(self, name: str, birth_year: int, gender: str, height: float, weight: float) -> tuple:
        for rec in self.db.records:
            if rec.name == name and rec.birth_year == birth_year:
                return False, "이미 존재하는 회원입니다."

        record_id = self.db.generate_id()
        bmi, status = self.calculate_bmi(height, weight)
        
        new_record = HealthRecord(
            record_id=record_id,
            name=name,
            birth_year=birth_year,
            gender=gender,
            height=height,
            weight=weight,
            bmi=bmi,
            status=status
        )
        
        self.db.add_record(new_record)
        return True, f"등록 성공 (식별번호: {record_id})"

    def get_all_records(self) -> list:
        return self.db.records

    def search_records(self, keyword: str) -> list:
        result = []
        keyword = keyword.strip().lower()
        for rec in self.db.records:
            if keyword in rec.id.lower() or keyword in rec.name.lower():
                result.append(rec)
        return result

    def update_record(self, record_id: str, name: str, birth_year: int, gender: str, height: float, weight: float) -> tuple:
        for rec in self.db.records:
            if rec.id == record_id:
                rec.name = name
                rec.birth_year = birth_year
                rec.gender = gender
                rec.height = height
                rec.weight = weight
                bmi, status = self.calculate_bmi(height, weight)
                rec.bmi = bmi
                rec.status = status
                return True, "수정 및 BMI 재계산 완료"
        return False, "해당 식별번호의 레코드를 찾을 수 없습니다."

    def delete_record(self, record_id: str) -> tuple:
        for i, rec in enumerate(self.db.records):
            if rec.id == record_id:
                del self.db.records[i]
                return True, "삭제 완료"
        return False, "해당 식별번호의 레코드를 찾을 수 없습니다."

    def get_statistics(self) -> dict:
        total_count = len(self.db.records)
        if total_count == 0:
            return {
                "total_count": 0,
                "avg_height": 0.0,
                "avg_weight": 0.0,
                "avg_bmi": 0.0
            }
        
        total_height = sum(rec.height for rec in self.db.records)
        total_weight = sum(rec.weight for rec in self.db.records)
        total_bmi = sum(rec.bmi for rec in self.db.records)
        
        return {
            "total_count": total_count,
            "avg_height": round(total_height / total_count, 2),
            "avg_weight": round(total_weight / total_count, 2),
            "avg_bmi": round(total_bmi / total_count, 2)
        }

    def save_data(self, filepath: str, file_type: str = "json"):
        if file_type == "json":
            self.db.save_to_json(filepath)
        elif file_type == "csv":
            self.db.save_to_csv(filepath)
        elif file_type == "txt":
            self.db.save_to_txt(filepath)
        elif file_type == "pkl":
            self.db.save_to_pkl(filepath)

    def load_data(self, filepath: str, file_type: str = "json"):
        if file_type == "json":
            return self.db.load_from_json(filepath)
        elif file_type == "csv":
            return self.db.load_from_csv(filepath)
        elif file_type == "txt":
            return self.db.load_from_txt(filepath)
        elif file_type == "pkl":
            return self.db.load_from_pkl(filepath)
        return []