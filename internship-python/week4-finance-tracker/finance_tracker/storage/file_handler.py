import json
import shutil
from datetime import datetime
from pathlib import Path
from finance_tracker.config import EXPENSES_FILE, BACKUP_DIR, MAX_BACKUP_COUNT
from finance_tracker.models.expense import Expense

def load_expenses():
    if not EXPENSES_FILE.exists():
        return []
    
    try:
        with open(EXPENSES_FILE, 'r') as f:
            data = json.load(f)
            return [Expense.from_dict(item) for item in data]
    except json.JSONDecodeError:
        print("Warning: Corrupted data file. Starting fresh.")
        return []
    except Exception as e:
        print(f"Error loading expenses: {e}")
        return []

def save_expenses(expenses):
    try:
        data = [expense.to_dict() for expense in expenses]
        with open(EXPENSES_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving expenses: {e}")
        return False

def create_backup():
    if not EXPENSES_FILE.exists():
        print("No data file to backup.")
        return False
    
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = BACKUP_DIR / f"expenses_backup_{timestamp}.json"
        shutil.copy2(EXPENSES_FILE, backup_file)
        
        # Keep only last MAX_BACKUP_COUNT backups
        cleanup_old_backups()
        
        print(f"Backup created: {backup_file.name}")
        return True
    except Exception as e:
        print(f"Backup failed: {e}")
        return False

def cleanup_old_backups():
    backups = sorted(BACKUP_DIR.glob("expenses_backup_*.json"))
    if len(backups) > MAX_BACKUP_COUNT:
        for old_backup in backups[:-MAX_BACKUP_COUNT]:
            old_backup.unlink()

def restore_from_backup(backup_file):
    try:
        backup_path = BACKUP_DIR / backup_file
        if not backup_path.exists():
            print("Backup file not found.")
            return False
        
        shutil.copy2(backup_path, EXPENSES_FILE)
        print("Data restored successfully.")
        return True
    except Exception as e:
        print(f"Restore failed: {e}")
        return False

def list_backups():
    backups = sorted(BACKUP_DIR.glob("expenses_backup_*.json"), reverse=True)
    if not backups:
        print("No backups found.")
        return []
    
    print("\nAvailable backups:")
    for i, backup in enumerate(backups, 1):
        print(f"{i}. {backup.name}")
    return backups

def export_to_csv(expenses, filename=None):
    import csv
    from finance_tracker.config import EXPORT_DIR
    
    if not expenses:
        print("No expenses to export.")
        return False
    
    try:
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"expenses_export_{timestamp}.csv"
        
        export_path = EXPORT_DIR / filename
        
        with open(export_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Amount', 'Category', 'Description'])
            for expense in expenses:
                writer.writerow([expense.date, expense.amount, expense.category, expense.description])
        
        print(f"Exported to: {export_path}")
        return True
    except Exception as e:
        print(f"Export failed: {e}")
        return False