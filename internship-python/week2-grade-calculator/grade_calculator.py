# Student grade calculator
# Week 2 Project - Control Flow & Data Structures
# Created by : Saiful Islam

def calculate_grade(average):
    """Calculate grade based on average marks"""
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', 'Very Good! You\'re doing well.'
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'

def get_valid_number(prompt, min_val=0, max_val=100):
    """Get a valid number within specified range"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input! Please enter a number.")

def save_results_to_file(student_names, student_results, filename="results.txt"):
    """Save results to a text file"""
    try:
        with open(filename, 'w') as file:
            file.write("=" * 60 + "\n")
            file.write("            STUDENT GRADE RESULTS\n")
            file.write("=" * 60 + "\n\n")
            file.write(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment\n")
            file.write("-" * 60 + "\n")
            
            for i in range(len(student_names)):
                name = student_names[i]
                avg = student_results[i]['average']
                grade = student_results[i]['grade']
                comment = student_results[i]['comment']
                file.write(f"{name:<20} | {avg:>5.1f} | {grade:^5} | {comment}\n")
            
            file.write("\n" + "=" * 60 + "\n")
        print(f"\n✓ Results saved to {filename}")
        return True
    except Exception as e:
        print(f"\n✗ Error saving file: {e}")
        return False

def search_student(student_names, student_results):
    """Search for a specific student"""
    search_name = input("\nEnter student name to search: ").strip()
    
    found = False
    for i in range(len(student_names)):
        if student_names[i].lower() == search_name.lower():
            found = True
            print("\n" + "=" * 50)
            print(f"Student Found: {student_names[i]}")
            print("=" * 50)
            print(f"Average: {student_results[i]['average']:.1f}")
            print(f"Grade: {student_results[i]['grade']}")
            print(f"Comment: {student_results[i]['comment']}")
            print("=" * 50)
            break
    
    if not found:
        print(f"\n✗ Student '{search_name}' not found!")

def main():
    """Main program function"""
    print("=" * 60)
    print("            STUDENT GRADE CALCULATOR")
    print("=" * 60)
    print()
    
    # Get number of students with validation
    while True:
        try:
            num_students = int(input("Enter number of students: "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
    
    # Initialize lists to store data
    student_names = []
    student_marks = []  # Will be list of lists
    student_results = []  # Will store dictionaries with results
    
    # Collect data for each student
    for i in range(num_students):
        print(f"\n{'='*30} STUDENT {i+1} {'='*30}")
        
        # Get student name
        name = input("Student name: ").strip()
        while name == "":
            print("Name cannot be empty!")
            name = input("Student name: ").strip()
        student_names.append(name)
        
        # Get marks for 3 subjects
        print("Enter marks (0-100):")
        math = get_valid_number("  Math: ")
        science = get_valid_number("  Science: ")
        english = get_valid_number("  English: ")
        
        # Store marks
        student_marks.append([math, science, english])
        
        # Calculate average
        average = (math + science + english) / 3
        
        # Get grade and comment
        grade, comment = calculate_grade(average)
        
        # Store results
        student_results.append({
            'average': average,
            'grade': grade,
            'comment': comment
        })
    
    # Display results
    print("\n" + "=" * 60)
    print("                    RESULTS SUMMARY")
    print("=" * 60)
    print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment")
    print("-" * 60)
    
    for i in range(num_students):
        name = student_names[i]
        avg = student_results[i]['average']
        grade = student_results[i]['grade']
        comment = student_results[i]['comment']
        
        print(f"{name:<20} | {avg:>5.1f} | {grade:^5} | {comment}")
    
    # Calculate and display statistics
    if num_students > 0:
        averages = [result['average'] for result in student_results]
        class_avg = sum(averages) / len(averages)
        max_avg = max(averages)
        min_avg = min(averages)
        max_index = averages.index(max_avg)
        min_index = averages.index(min_avg)
        
        print("\n" + "=" * 60)
        print("                  CLASS STATISTICS")
        print("=" * 60)
        print(f"Total Students: {num_students}")
        print(f"Class Average: {class_avg:.1f}")
        print(f"Highest Average: {max_avg:.1f} ({student_names[max_index]})")
        print(f"Lowest Average: {min_avg:.1f} ({student_names[min_index]})")
        print("=" * 60)
    
    # Menu for additional operations
    while True:
        print("\n" + "=" * 60)
        print("OPTIONS:")
        print("1. Search for a student")
        print("2. Save results to file")
        print("3. Exit")
        print("=" * 60)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            search_student(student_names, student_results)
        elif choice == '2':
            save_results_to_file(student_names, student_results)
        elif choice == '3':
            print("\n" + "=" * 60)
            print("Thank you for using the Grade Calculator!")
            print("=" * 60)
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()