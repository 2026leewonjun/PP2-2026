import json
import csv
import pickle
import os

class HealthRecord:
    def __init__(self, record_id: str, name: str, birth_year: int, gender: str, 
                 height: float, weight: float, bmi: float = 0.0, status: str = ""):
        self.id = record_id
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bmi = bmi
        self.status = status

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "bmi": self.bmi,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            record_id=data.get("id", ""),
            name=data.get("name", ""),
            birth_year=int(data.get("birth_year", 0)),
            gender=data.get("gender", ""),
            height=float(data.get("height", 0.0)),
            weight=float(data.get("weight", 0.0)),
            bmi=float(data.get("bmi", 0.0)),
            status=data.get("status", "")
        )


class HealthDB:
    def __init__(self):
        self.records = []
        self.id_counter = 1

    def generate_id(self, year_prefix: str = "P2026") -> str:
        new_id = f"{year_prefix}-{self.id_counter:04d}"
        self.id_counter += 1
        return new_id

    def add_record(self, record: HealthRecord):
        self.records.append(record)

    def save_to_json(self, filepath: str):
        try:
            data = [rec.to_dict() for rec in self.records]
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"[오류] JSON 저장 실패: {e}")

    def load_from_json(self, filepath: str):
        if not os.path.exists(filepath):
            return []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.records = [HealthRecord.from_dict(d) for d in data]
                self._update_id_counter()
                return self.records
        except Exception as e:
            print(f"[오류] JSON 로드 실패: {e}")
            return []

    def save_to_csv(self, filepath: str):
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            fieldnames = ["id", "name", "birth_year", "gender", "height", "weight", "bmi", "status"]
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for rec in self.records:
                    writer.writerow(rec.to_dict())
        except Exception as e:
            print(f"[오류] CSV 저장 실패: {e}")

    def load_from_csv(self, filepath: str):
        if not os.path.exists(filepath):
            return []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.records = [HealthRecord.from_dict(row) for row in reader]
                self._update_id_counter()
                return self.records
        except Exception as e:
            print(f"[오류] CSV 로드 실패: {e}")
            return []

    def save_to_txt(self, filepath: str):
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                for rec in self.records:
                    line = f"{rec.id},{rec.name},{rec.birth_year},{rec.gender},{rec.height},{rec.weight},{rec.bmi},{rec.status}\n"
                    f.write(line)
        except Exception as e:
            print(f"[오류] TXT 저장 실패: {e}")

    def load_from_txt(self, filepath: str):
        if not os.path.exists(filepath):
            return []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.records = []
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(',')
                    if len(parts) == 8:
                        data = {
                            "id": parts[0], "name": parts[1], "birth_year": parts[2],
                            "gender": parts[3], "height": parts[4], "weight": parts[5],
                            "bmi": parts[6], "status": parts[7]
                        }
                        self.records.append(HealthRecord.from_dict(data))
                self._update_id_counter()
                return self.records
        except Exception as e:
            print(f"[오류] TXT 로드 실패: {e}")
            return []

    def save_to_pkl(self, filepath: str):
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'wb') as f:
                pickle.dump(self.records, f)
        except Exception as e:
            print(f"[오류] PKL 저장 실패: {e}")

    def load_from_pkl(self, filepath: str):
        if not os.path.exists(filepath):
            return []
        try:
            with open(filepath, 'rb') as f:
                self.records = pickle.load(f)
                self._update_id_counter()
                return self.records
        except Exception as e:
            print(f"[오류] PKL 로드 실패: {e}")
            return []

    def _update_id_counter(self):
        max_num = 0
        for rec in self.records:
            if rec.id and '-' in rec.id:
                try:
                    num = int(rec.id.split('-')[-1])
                    if num > max_num:
                        max_num = num
                except ValueError:
                    pass
        self.id_counter = max_num + 1