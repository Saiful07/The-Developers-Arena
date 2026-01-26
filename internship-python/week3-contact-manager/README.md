# Contact Management System

A Python-based contact management system for storing and managing phone contacts with persistent JSON storage.

## Features

- ✅ Add new contacts with phone validation
- 🔍 Search contacts by partial name matching
- ✏️ Update existing contact information
- 🗑️ Delete contacts with confirmation
- 📋 Display all contacts in formatted list
- 💾 Automatic save/load from JSON file
- 📊 Export contacts to CSV
- 📈 Contact statistics and analytics

## Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)

## Installation

1. Clone this repository
2. Navigate to the project directory
3. Run the program:
```bash
python contacts_manager.py
```

## Usage

The program provides an interactive menu with the following options:

1. **Add Contact** - Add a new contact with name and 10-digit phone number
2. **Search Contacts** - Search by partial name match (case-insensitive)
3. **Update Contact** - Modify existing contact's phone number
4. **Delete Contact** - Remove a contact (with confirmation)
5. **Display All Contacts** - View all saved contacts
6. **Export to CSV** - Export contacts to a CSV file
7. **Show Statistics** - View contact statistics and area code distribution
8. **Exit** - Save and exit the program

## Phone Number Format

- Accepts 10-digit US phone numbers
- Automatically strips dashes, spaces, and parentheses
- Formats display as: (XXX) XXX-XXXX

## Data Storage

Contacts are stored in `contacts_data.json` in the following format:
```json
{
  "John Doe": "5551234567",
  "Jane Smith": "5559876543"
}
```

## Testing

Run the test suite to verify functionality:
```bash
python test_contacts.py
```

Tests cover:
- Phone number validation
- Contact search functionality
- File save/load operations
- Edge cases and error handling

## Project Structure
```
week3-contact-manager/
├── contacts_manager.py    # Main program
├── contacts_data.json     # Contact storage (auto-generated)
├── test_contacts.py       # Test suite
├── README.md             # Documentation
├── requirements.txt      # Python dependencies
```

## Error Handling

The system handles:
- Invalid phone number formats
- Duplicate contact names
- Missing or corrupted data files
- Invalid menu selections
- Empty input fields

## Author

Week 3 Python Internship Assignment
```

### requirements.txt
```
# No external dependencies required
# All functionality uses Python standard library

# Optional: For running tests with pytest
# pytest>=7.4.0
```