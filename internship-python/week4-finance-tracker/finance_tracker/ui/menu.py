from datetime import datetime
from finance_tracker.core.expense_manager import ExpenseManager
from finance_tracker.core.validators import (
    validate_amount, validate_date, validate_category, 
    validate_description, get_validated_input, ValidationError
)
from finance_tracker.reporting.report_generator import ReportGenerator
from finance_tracker.storage.file_handler import (
    create_backup, restore_from_backup, list_backups, export_to_csv
)
from finance_tracker.config import DEFAULT_CATEGORIES, DATE_FORMAT

class MenuSystem:
    def __init__(self):
        self.manager = ExpenseManager()
        self.reporter = ReportGenerator(self.manager)
    
    def run(self):
        print("=" * 60)
        print("          PERSONAL FINANCE TRACKER")
        print("=" * 60)
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (0-9): ").strip()
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.search_expenses()
            elif choice == '4':
                self.generate_monthly_report()
            elif choice == '5':
                self.view_category_breakdown()
            elif choice == '6':
                self.view_statistics()
            elif choice == '7':
                self.export_data()
            elif choice == '8':
                self.backup_restore()
            elif choice == '0':
                print("\n" + "=" * 60)
                print("Thank you for using Personal Finance Tracker!")
                print("=" * 60)
                break
            else:
                print("Invalid choice! Please enter 0-8.")
    
    def display_menu(self):
        print("\n" + "=" * 40)
        print("              MAIN MENU")
        print("=" * 40)
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Search Expenses")
        print("4. Generate Monthly Report")
        print("5. View Category Breakdown")
        print("6. View Statistics")
        print("7. Export Data to CSV")
        print("8. Backup/Restore Data")
        print("0. Exit")
        print("=" * 40)
    
    def add_expense(self):
        print("\n--- ADD NEW EXPENSE ---")
        
        # Get today's date as default
        today = datetime.now().strftime(DATE_FORMAT)
        date_input = input(f"Enter date ({DATE_FORMAT}) [Press Enter for today]: ").strip()
        if not date_input:
            date = today
        else:
            date = get_validated_input(f"Date ({DATE_FORMAT}): ", validate_date)
            if date is None:
                return
        
        amount = get_validated_input("Amount (₹): ", validate_amount)
        if amount is None:
            return
        
        print("\nAvailable categories:")
        for i, cat in enumerate(DEFAULT_CATEGORIES, 1):
            print(f"{i}. {cat}")
        
        cat_choice = input("Select category (1-8): ").strip()
        try:
            cat_index = int(cat_choice) - 1
            if 0 <= cat_index < len(DEFAULT_CATEGORIES):
                category = DEFAULT_CATEGORIES[cat_index]
            else:
                print("Invalid category selection.")
                return
        except ValueError:
            print("Invalid input.")
            return
        
        description = get_validated_input("Description: ", validate_description)
        if description is None:
            return
        
        expense = self.manager.add_expense(date, amount, category, description)
        if expense:
            print(f"\n✓ Expense added successfully!")
            print(f"  {expense}")
        else:
            print("Failed to save expense.")
    
    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        expenses = self.manager.get_all_expenses()
        
        if not expenses:
            print("No expenses recorded yet.")
            return
        
        print(f"\nTotal: {len(expenses)} expenses")
        print("-" * 80)
        for expense in expenses:
            print(expense)
        print("-" * 80)
    
    def search_expenses(self):
        print("\n--- SEARCH EXPENSES ---")
        print("1. Search by category")
        print("2. Search by date range")
        print("3. Search by description")
        print("0. Back")
        
        choice = input("\nSelect search type: ").strip()
        
        if choice == '1':
            print("\nCategories:")
            for i, cat in enumerate(DEFAULT_CATEGORIES, 1):
                print(f"{i}. {cat}")
            cat_choice = input("Select category: ").strip()
            try:
                cat_index = int(cat_choice) - 1
                if 0 <= cat_index < len(DEFAULT_CATEGORIES):
                    results = self.manager.search_expenses(category=DEFAULT_CATEGORIES[cat_index])
                else:
                    print("Invalid selection.")
                    return
            except ValueError:
                print("Invalid input.")
                return
        
        elif choice == '2':
            start = input(f"Start date ({DATE_FORMAT}): ").strip()
            end = input(f"End date ({DATE_FORMAT}): ").strip()
            results = self.manager.search_expenses(start_date=start, end_date=end)
        
        elif choice == '3':
            keyword = input("Enter keyword: ").strip()
            results = self.manager.search_expenses(description=keyword)
        
        else:
            return
        
        print(f"\nFound {len(results)} expenses:")
        print("-" * 80)
        for expense in results:
            print(expense)
        print("-" * 80)
    
    def generate_monthly_report(self):
        print("\n--- MONTHLY REPORT ---")
        year_input = input("Enter year (YYYY): ").strip()
        month_input = input("Enter month (1-12): ").strip()
        
        try:
            year = int(year_input)
            month = int(month_input)
            if not (1 <= month <= 12):
                print("Month must be between 1 and 12.")
                return
            
            self.reporter.generate_monthly_report(year, month)
        except ValueError:
            print("Invalid year or month.")
    
    def view_category_breakdown(self):
        self.reporter.generate_category_breakdown()
    
    def view_statistics(self):
        self.reporter.generate_statistics()
    
    def export_data(self):
        print("\n--- EXPORT DATA ---")
        expenses = self.manager.get_all_expenses()
        
        if export_to_csv(expenses):
            print("Export completed successfully!")
    
    def backup_restore(self):
        print("\n--- BACKUP/RESTORE ---")
        print("1. Create backup")
        print("2. Restore from backup")
        print("0. Back")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            create_backup()
        elif choice == '2':
            backups = list_backups()
            if not backups:
                return
            
            selection = input("\nEnter backup number to restore (or 0 to cancel): ").strip()
            try:
                idx = int(selection) - 1
                if 0 <= idx < len(backups):
                    confirm = input("This will overwrite current data. Continue? (yes/no): ").strip().lower()
                    if confirm == 'yes':
                        restore_from_backup(backups[idx].name)
                        # Reload expenses after restore
                        self.manager = ExpenseManager()
                        self.reporter = ReportGenerator(self.manager)
            except ValueError:
                print("Invalid input.")