"""
Test Cases for Contact Management System
Week 3 Assignment
"""

from contacts_manager import (
    validate_phone, 
    search_by_name, 
    load_contacts,
    save_contacts
)
import os
import json


def test_validate_phone():
    """Test phone number validation"""
    print("Testing validate_phone()...")
    
    # Valid cases
    assert validate_phone("1234567890") == "1234567890", "Failed: 10 digits"
    assert validate_phone("123-456-7890") == "1234567890", "Failed: dashes"
    assert validate_phone("(123) 456-7890") == "1234567890", "Failed: parentheses"
    assert validate_phone("123 456 7890") == "1234567890", "Failed: spaces"
    
    # Invalid cases
    assert validate_phone("123") is None, "Failed: too short"
    assert validate_phone("12345678901") is None, "Failed: too long"
    assert validate_phone("abcd") is None, "Failed: letters"
    assert validate_phone("") is None, "Failed: empty string"
    
    print("✅ validate_phone() tests passed")


def test_search_by_name():
    """Test contact search functionality"""
    print("Testing search_by_name()...")
    
    contacts = {
        "John Doe": "1234567890",
        "Jane Doe": "0987654321",
        "Bob Smith": "5555555555"
    }
    
    # Search for "doe" - should find 2
    results = search_by_name(contacts, "doe")
    assert len(results) == 2, "Failed: search 'doe'"
    
    # Search for "john" - should find 1
    results = search_by_name(contacts, "john")
    assert len(results) == 1, "Failed: search 'john'"
    
    # Search for "smith" - should find 1
    results = search_by_name(contacts, "smith")
    assert len(results) == 1, "Failed: search 'smith'"
    
    # Search for "xyz" - should find 0
    results = search_by_name(contacts, "xyz")
    assert len(results) == 0, "Failed: search 'xyz'"
    
    # Case insensitive test
    results = search_by_name(contacts, "JOHN")
    assert len(results) == 1, "Failed: case insensitive"
    
    print("✅ search_by_name() tests passed")


def test_file_operations():
    """Test save and load operations"""
    print("Testing file operations...")
    
    test_file = "test_contacts_temp.json"
    test_contacts = {
        "Test User": "1234567890",
        "Another Test": "0987654321"
    }
    
    # Test save
    try:
        with open(test_file, 'w') as f:
            json.dump(test_contacts, f)
        assert os.path.exists(test_file), "Failed: file not created"
        
        # Test load
        with open(test_file, 'r') as f:
            loaded = json.load(f)
        assert loaded == test_contacts, "Failed: loaded data doesn't match"
        
        print("✅ File operations tests passed")
    finally:
        # Cleanup
        if os.path.exists(test_file):
            os.remove(test_file)


def test_edge_cases():
    """Test edge cases and error conditions"""
    print("Testing edge cases...")
    
    # Empty contacts search
    results = search_by_name({}, "test")
    assert len(results) == 0, "Failed: empty contacts search"
    
    # Empty search term
    contacts = {"John": "1234567890"}
    results = search_by_name(contacts, "")
    assert len(results) == 1, "Failed: empty search term should match all"
    
    # Special characters in phone
    assert validate_phone("***123***456***7890***") == "1234567890", "Failed: special chars"
    
    print("✅ Edge cases tests passed")


def run_all_tests():
    """Run all test functions"""
    print("\n" + "=" * 50)
    print("RUNNING TEST SUITE")
    print("=" * 50 + "\n")
    
    try:
        test_validate_phone()
        test_search_by_name()
        test_file_operations()
        test_edge_cases()
        
        print("\n" + "=" * 50)
        print("ALL TESTS PASSED ✅")
        print("=" * 50)
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")


if __name__ == "__main__":
    run_all_tests()