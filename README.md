# Student Management System

This is a simple command-line Student Management System built with Python.  
The program lets users add, view, update, and delete student records while storing the data in a JSON file.

I built this project to practice core Python concepts like functions, loops, input validation, and working with files. It also helped me understand how a small data management system can be structured in a clean and interactive way.

---

## What the Program Can Do

With this system you can:

• Add new students  
• View all students currently stored  
• Update existing student information  
• Delete students from the system  
• Save student records to a JSON file  

Each student record contains:

- Student ID
- Name
- Age
- Grade

---

## How the Data Is Stored

While the program is running, student information is stored in a list of dictionaries.

Example student record:

```
{
  "ID": 101,
  "Name": "John",
  "Age": 20,
  "Grade": 90
}
```

When you choose **Save & Exit**, the program writes all student records to a file called:

```
students.json
```

This allows the data to be saved even after the program closes.

---

## Menu Options

When the program starts, you'll see the following menu:

```
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Save & Exit
```

You can keep managing student records until you choose to exit.

---

## How to Run the Program

1. Make sure Python 3 is installed.

2. Clone the repository

```
git clone https://github.com/yourusername/student-management-system.git
```

3. Navigate to the project folder

```
cd student-management-system
```

4. Run the program

```
python main.py
```

---

## Future Improvements

Some ideas to expand this project in the future:

• Automatically load saved students when the program starts  
• Add a search feature (by ID or name)  
• Show grade statistics like average or highest score  
• Build a graphical interface instead of a command-line menu  
• Store data in a database instead of JSON  

---

## Author

Ahmad Zayour  
Software Developer  

GitHub: https://github.com/azayour
