# Student Record System

A simple command-line application for managing student records. This Python-based system allows you to add, view, update, and delete student information, with data persistence using JSON file storage.

## Features

- ✅ **Add Student Records**: Add new students with their details (name, ID, age, course, marks)
- 📋 **View All Students**: Display all student records in a formatted table
- ✏️ **Update Student Information**: Modify existing student details by student ID
- 🗑️ **Delete Student Records**: Remove student records from the system
- 💾 **Data Persistence**: All data is stored in a JSON file (`data.json`)

## Requirements

- Python 3.10 or higher (for `match-case` statement support)
- No external dependencies required (uses only Python standard library)

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.10+ installed on your system
3. No additional packages need to be installed

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Follow the menu prompts:
   - Press `1` to add a new student
   - Press `2` to view all student records
   - Press `3` to update a student's information
   - Press `4` to delete a student record
   - Press `5` to exit the application

## Project Structure

```
Student-Record-System/
│
├── main.py          # Main application file with all functionality
├── data.json        # JSON file storing student records
└── README.md        # Project documentation
```

## Student Data Structure

Each student record contains the following fields:
- `s_name`: Student's name (string)
- `s_id`: Student ID (integer)
- `s_age`: Student's age (integer)
- `s_course`: Enrolled course (string)
- `s_marks`: Obtained marks (integer)

## Example Usage

### Adding a Student
```
Enter the student name: John Doe
Enter the student id: 101
Enter the age of the student: 20
Enter the enrolled course of the student: Computer Science
Enter the obtain marks of the student: 85
```

### Viewing All Students
The system displays all students in a formatted table:
```
======================================================================
ID       Name                 Age    Course               Marks 
======================================================================
101      John Doe             20     Computer Science      85    
```

## Features in Detail

### Add Student
- Prompts for student name, ID, age, course, and marks
- Automatically saves to `data.json`
- Handles cases where the JSON file doesn't exist yet

### View All Students
- Displays all student records in a clean, formatted table
- Shows a message if no data exists

### Update Student
- Find student by ID
- Update name, age, course, and marks
- Confirms successful update

### Delete Student
- Remove student by ID
- Confirms successful deletion

## Notes

- The application uses a JSON file (`data.json`) for data storage
- If the JSON file doesn't exist, it will be created automatically
- Student IDs should be unique for proper record management
- The application runs in a loop until you choose option 5 to exit

## Future Enhancements

Potential improvements for this project:
- GUI interface using tkinter or web interface
- Database integration (SQLite, MySQL, etc.)


## Author

Developed as part of the Weintern Student Record System project.

