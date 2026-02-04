from datetime import datetime
from finance_tracker.models.expense import Expense
from finance_tracker.storage.file_handler import load_expenses, save_expenses

class ExpenseManager:
    def __init__(self):
        self.expenses = load_expenses()
    
    def add_expense(self, date, amount, category, description):
        expense = Expense(
            date=date,
            amount=amount,
            category=category,
            description=description
        )
        self.expenses.append(expense)
        if save_expenses(self.expenses):
            return expense
        return None
    
    def get_all_expenses(self):
        return sorted(self.expenses, key=lambda x: x.date, reverse=True)
    
    def search_expenses(self, **kwargs):
        results = self.expenses
        
        if 'category' in kwargs and kwargs['category']:
            results = [e for e in results if e.category == kwargs['category']]
        
        if 'start_date' in kwargs and kwargs['start_date']:
            results = [e for e in results if e.date >= kwargs['start_date']]
        
        if 'end_date' in kwargs and kwargs['end_date']:
            results = [e for e in results if e.date <= kwargs['end_date']]
        
        if 'description' in kwargs and kwargs['description']:
            keyword = kwargs['description'].lower()
            results = [e for e in results if keyword in e.description.lower()]
        
        return sorted(results, key=lambda x: x.date, reverse=True)
    
    def get_expenses_by_month(self, year, month):
        month_str = f"{year}-{month:02d}"
        return [e for e in self.expenses if e.date.startswith(month_str)]
    
    def get_category_totals(self):
        totals = {}
        for expense in self.expenses:
            totals[expense.category] = totals.get(expense.category, 0) + expense.amount
        return totals
    
    def get_total_expenses(self):
        return sum(e.amount for e in self.expenses)
    
    def delete_expense(self, expense_id):
        original_count = len(self.expenses)
        self.expenses = [e for e in self.expenses if e.id != expense_id]
        
        if len(self.expenses) < original_count:
            save_expenses(self.expenses)
            return True
        return False