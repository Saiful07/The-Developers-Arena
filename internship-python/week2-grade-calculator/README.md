# Student Grade Calculator

This is my Week 2 project for the Developers Arena internship. I built a Python program that calculates student grades, handles multiple students at once, and gives you stats about the whole class.

## What it does

The program lets you enter marks for multiple students (math, science, and english), then it calculates their average and assigns a grade. It also shows you class statistics like the highest and lowest scores, plus you can search for specific students or save everything to a file.

I used everything we learned in Week 2 - conditionals, lists, loops, and error handling. The program validates all inputs so you can't break it by entering weird values.

## How the grading works

- **A (90-100)**: Excellent! Keep up the great work!
- **B (80-89)**: Very Good! You're doing well.
- **C (70-79)**: Good. Room for improvement.
- **D (60-69)**: Needs Improvement. Please study more.
- **F (below 60)**: Failed. Please seek help from teacher.

## Running the program

You'll need Python 3 installed. Then just run:

```bash
python grade_calculator.py
```

The program will ask you how many students you want to enter, then for each student it asks for their name and marks in three subjects. After collecting everything, it shows a nice table with all the results and some statistics.

## Features I added

- Input validation - won't let you enter invalid numbers or blank names
- Search function to find specific students
- Save results to a text file
- Menu system to navigate different options
- Class statistics showing average, highest, and lowest scores
- Formatted table output that's easy to read

## What I learned

This project really helped me understand how to use loops properly, especially the difference between `for` and `while` loops. The input validation was tricky at first but using try-except blocks made it much cleaner. I also got better at working with lists and dictionaries together.

The hardest part was probably formatting the output table to look nice and aligned. I had to learn about string formatting with f-strings and padding.

## Files in this repo

- `grade_calculator.py` - the main program
- `test_students.txt` - some test cases I used
- `results_sample.txt` - example output from running the program

## Future improvements

If I had more time, I'd add:
- More subjects (right now it's just 3)
- Ability to load student data from a CSV file
- Better error messages
- Option to edit a student's marks after entering them

---

**Saiful**  
Developers Arena Internship - Week 2  
January 2026