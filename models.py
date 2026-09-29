from dataclasses import dataclass, asdict
from typing import Dict, Any

@dataclass
class Expense:
    id: int
    name: str
    amount: float
    category: str
    date: str
    note: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Expense":
        return Expense(
            id=int(data["id"]), name=str(data["name"]),
            amount=float(data["amount"]), category=str(data["category"]),
            date=str(data["date"]), note=str(data.get("note", ""))
        )

@dataclass
class Budget:
    category: str
    limit: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
