from datetime import datetime
from finance_tracker.config import CURRENCY_SYMBOL

class ReportGenerator:
    def __init__(self, expense_manager):
        self.manager = expense_manager
    
    def generate_monthly_report(self, year, month):
        expenses = self.manager.get_expenses_by_month(year, month)
        
        if not expenses:
            print(f"\nNo expenses found for {year}-{month:02d}")
            return
        
        total = sum(e.amount for e in expenses)
        
        print("\n" + "=" * 60)
        print(f"MONTHLY REPORT: {year}-{month:02d}")
        print("=" * 60)
        print(f"Total Expenses: {CURRENCY_SYMBOL}{total:,.2f}")
        print(f"Number of Transactions: {len(expenses)}")
        print(f"Average per Transaction: {CURRENCY_SYMBOL}{total/len(expenses):,.2f}")
        
        # Category breakdown for the month
        categories = {}
        for expense in expenses:
            categories[expense.category] = categories.get(expense.category, 0) + expense.amount
        
        print("\nCategory Breakdown:")
        print("-" * 60)
        for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total) * 100
            print(f"{category:.<30} {CURRENCY_SYMBOL}{amount:>10,.2f} ({percentage:>5.1f}%)")
        
        print("=" * 60)
    
    def generate_category_breakdown(self):
        totals = self.manager.get_category_totals()
        
        if not totals:
            print("\nNo expenses recorded yet.")
            return
        
        grand_total = sum(totals.values())
        
        print("\n" + "=" * 60)
        print("CATEGORY BREAKDOWN (All Time)")
        print("=" * 60)
        print(f"Total Expenses: {CURRENCY_SYMBOL}{grand_total:,.2f}")
        print("\nBreakdown:")
        print("-" * 60)
        
        for category, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / grand_total) * 100
            bar_length = int(percentage / 2)
            bar = "█" * bar_length
            print(f"{category:.<30} {CURRENCY_SYMBOL}{amount:>10,.2f} ({percentage:>5.1f}%)")
            print(f"{' ':30} {bar}")
        
        print("=" * 60)
    
    def generate_statistics(self):
        expenses = self.manager.get_all_expenses()
        
        if not expenses:
            print("\nNo expenses recorded yet.")
            return
        
        total = self.manager.get_total_expenses()
        avg = total / len(expenses)
        
        amounts = sorted([e.amount for e in expenses])
        median = amounts[len(amounts)//2] if len(amounts) % 2 else (amounts[len(amounts)//2-1] + amounts[len(amounts)//2]) / 2
        
        print("\n" + "=" * 60)
        print("EXPENSE STATISTICS")
        print("=" * 60)
        print(f"Total Expenses: {CURRENCY_SYMBOL}{total:,.2f}")
        print(f"Total Transactions: {len(expenses)}")
        print(f"Average Expense: {CURRENCY_SYMBOL}{avg:,.2f}")
        print(f"Median Expense: {CURRENCY_SYMBOL}{median:,.2f}")
        print(f"Highest Expense: {CURRENCY_SYMBOL}{max(amounts):,.2f}")
        print(f"Lowest Expense: {CURRENCY_SYMBOL}{min(amounts):,.2f}")
        
        # Date range
        dates = sorted([e.date for e in expenses])
        print(f"\nDate Range: {dates[0]} to {dates[-1]}")
        
        print("=" * 60)