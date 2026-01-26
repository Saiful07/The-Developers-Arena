"""
Contact Management System
Week 3 Assignment - Functions & Dictionaries
"""

import json
import os

# Configuration
DATA_FILE = "contacts_data.json"


def validate_phone(phone):
    """
    Validate phone number format (10 digits only)
    Returns cleaned phone number or None if invalid
    """
    digits = ''.join(filter(str.isdigit, phone))
    if len(digits) == 10:
        return digits
    return None


def load_contacts():
    """Load contacts from JSON file"""
    if not os.path.exists(DATA_FILE):
        return {}
    
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: {DATA_FILE} is corrupted. Starting with empty contacts.")
        return {}
    except Exception as e:
        print(f"Error loading contacts: {e}")
        return {}


def save_contacts(contacts):
    """Save contacts to JSON file"""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(contacts, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving contacts: {e}")
        return False


def add_contact(contacts):
    """Add a new contact to the dictionary"""
    print("\n--- ADD CONTACT ---")
    
    name = input("Enter name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    
    if name in contacts:
        print(f"Error: Contact '{name}' already exists.")
        choice = input("Update existing contact? (y/n): ").lower()
        if choice == 'y':
            update_contact(contacts, name)
        return
    
    phone = input("Enter phone number (10 digits): ").strip()
    validated_phone = validate_phone(phone)
    
    if not validated_phone:
        print("Error: Invalid phone number. Must be exactly 10 digits.")
        return
    
    contacts[name] = validated_phone
    
    if save_contacts(contacts):
        print(f"✅ Contact '{name}' added successfully.")
    else:
        print("Warning: Contact added but failed to save to file.")


def search_contacts(contacts):
    """Search contacts by partial name match"""
    print("\n--- SEARCH CONTACTS ---")
    
    if not contacts:
        print("No contacts available.")
        return
    
    search_term = input("Enter name to search: ").strip()
    if not search_term:
        print("Error: Search term cannot be empty.")
        return
    
    results = search_by_name(contacts, search_term)
    display_search_results(results, search_term)


def search_by_name(contacts, term):
    """
    Search contacts dictionary by partial name match
    Returns dictionary of matching contacts
    """
    term_lower = term.lower()
    return {name: phone for name, phone in contacts.items() 
            if term_lower in name.lower()}


def display_search_results(results, search_term):
    """Display formatted search results"""
    if not results:
        print(f"No contacts found matching '{search_term}'.")
        return
    
    print(f"\nFound {len(results)} contact(s) matching '{search_term}':")
    print("-" * 50)
    for i, (name, phone) in enumerate(results.items(), 1):
        formatted_phone = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
        print(f"{i}. {name}: {formatted_phone}")
    print("-" * 50)


def update_contact(contacts, name=None):
    """Update an existing contact's phone number"""
    print("\n--- UPDATE CONTACT ---")
    
    if not contacts:
        print("No contacts available to update.")
        return
    
    if name is None:
        name = input("Enter name of contact to update: ").strip()
    
    if not name:
        print("Error: Name cannot be empty.")
        return
    
    if name not in contacts:
        print(f"Error: Contact '{name}' not found.")
        choice = input("Search for similar names? (y/n): ").lower()
        if choice == 'y':
            results = search_by_name(contacts, name)
            display_search_results(results, name)
        return
    
    print(f"Current phone: {contacts[name]}")
    new_phone = input("Enter new phone number (10 digits): ").strip()
    
    validated_phone = validate_phone(new_phone)
    if not validated_phone:
        print("Error: Invalid phone number. Must be exactly 10 digits.")
        return
    
    contacts[name] = validated_phone
    
    if save_contacts(contacts):
        print(f"✅ Contact '{name}' updated successfully.")
    else:
        print("Warning: Contact updated but failed to save to file.")


def delete_contact(contacts):
    """Delete a contact from the dictionary"""
    print("\n--- DELETE CONTACT ---")
    
    if not contacts:
        print("No contacts available to delete.")
        return
    
    name = input("Enter name of contact to delete: ").strip()
    
    if not name:
        print("Error: Name cannot be empty.")
        return
    
    if name not in contacts:
        print(f"Error: Contact '{name}' not found.")
        choice = input("Search for similar names? (y/n): ").lower()
        if choice == 'y':
            results = search_by_name(contacts, name)
            display_search_results(results, name)
        return
    
    # Confirmation
    print(f"Contact: {name}")
    print(f"Phone: {contacts[name]}")
    confirm = input("Are you sure you want to delete this contact? (y/n): ").lower()
    
    if confirm == 'y':
        del contacts[name]
        if save_contacts(contacts):
            print(f"✅ Contact '{name}' deleted successfully.")
        else:
            print("Warning: Contact deleted but failed to save to file.")
    else:
        print("Delete operation cancelled.")


def display_all_contacts(contacts):
    """Display all contacts in a formatted list"""
    print("\n--- ALL CONTACTS ---")
    
    if not contacts:
        print("No contacts available.")
        return
    
    print(f"Total contacts: {len(contacts)}")
    print("-" * 50)
    
    for i, (name, phone) in enumerate(sorted(contacts.items()), 1):
        formatted_phone = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
        print(f"{i}. {name}: {formatted_phone}")
    
    print("-" * 50)


def export_to_csv(contacts):
    """Export contacts to CSV file"""
    print("\n--- EXPORT TO CSV ---")
    
    if not contacts:
        print("No contacts available to export.")
        return
    
    filename = input("Enter CSV filename (default: contacts.csv): ").strip()
    if not filename:
        filename = "contacts.csv"
    
    if not filename.endswith('.csv'):
        filename += '.csv'
    
    try:
        import csv
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Phone'])
            for name, phone in sorted(contacts.items()):
                formatted_phone = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
                writer.writerow([name, formatted_phone])
        print(f"✅ Contacts exported to {filename}")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")


def show_statistics(contacts):
    """Display contact statistics"""
    print("\n--- STATISTICS ---")
    
    if not contacts:
        print("No contacts available.")
        return
    
    total = len(contacts)
    
    # Count unique area codes
    area_codes = {}
    for phone in contacts.values():
        area_code = phone[:3]
        area_codes[area_code] = area_codes.get(area_code, 0) + 1
    
    print(f"Total contacts: {total}")
    print(f"Unique area codes: {len(area_codes)}")
    
    if area_codes:
        print("\nArea code distribution:")
        for area_code, count in sorted(area_codes.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total) * 100
            print(f"  ({area_code}): {count} contacts ({percentage:.1f}%)")


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("CONTACT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Contact")
    print("2. Search Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Export to CSV")
    print("7. Show Statistics")
    print("8. Exit")
    print("=" * 50)


def main():
    """Main program loop"""
    print("Loading contacts...")
    contacts = load_contacts()
    print(f"Loaded {len(contacts)} contact(s).")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            display_all_contacts(contacts)
        elif choice == '6':
            export_to_csv(contacts)
        elif choice == '7':
            show_statistics(contacts)
        elif choice == '8':
            print("\nSaving contacts...")
            if save_contacts(contacts):
                print("✅ Contacts saved successfully.")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()