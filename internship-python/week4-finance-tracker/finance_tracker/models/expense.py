from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass
class Expense:
    date: str
    amount: float
    category: str
    description: str
    id: str = None
    
    def __post_init__(self):
        if self.id is None:
            self.id = self._generate_id()
    
    def _generate_id(self):
        # Simple ID based on timestamp
        return datetime.now().strftime("%Y%m%d%H%M%S%f")
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'amount': self.amount,
            'category': self.category,
            'description': self.description
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            date=data['date'],
            amount=data['amount'],
            category=data['category'],
            description=data['description']
        )
    
    def __str__(self):
        from finance_tracker.config import CURRENCY_SYMBOL
        return f"{self.date} | {CURRENCY_SYMBOL}{self.amount:.2f} | {self.category} | {self.description}"