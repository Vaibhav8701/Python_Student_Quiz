# Project Title:
Python Tkinter-Based Login, Registration, and Quiz System

# Overview:
This is a GUI-based application developed using Python’s Tkinter library. It allows a user to log in, fill out a registration form, and take a multiple-choice quiz with a countdown timer. The application features validation, structured navigation, and dynamic UI components.

# Modules & Flow:
#1. Login Window
Purpose: Authenticates users before allowing access to the registration and quiz.

Valid Credentials:

Email: Admin

Password: Abcd@1234

#Features:

Email & password input

Show/hide password

Validation using simple hardcoded logic

Redirects to registration window upon successful login

#2. Registration Form
Purpose: Collects user's personal and educational details before allowing access to the quiz.

Fields Collected:

First Name, Last Name

Father’s Name, Mother’s Name

Gender (Radio Buttons)

Qualification (Radio Buttons)

Skills (Checkbuttons: Python, Java, C++, SQL)

State and City (Dynamic Comboboxes)

Features:

All fields are required with validation

Selected data is written to a file demo.txt

Displays a summary message after submission

Disables quiz access until registration is completed

Uses partial() to handle function arguments

#3. Quiz Window
Purpose: Conducts a multiple-choice quiz based on questions loaded from a JSON file.

JSON Format:

question: List of questions

options: List of lists for each question's options

answer: List of correct answers (by index)

Features:

Timer (hour, minute, second) countdown

Displays questions and 4 options with radio buttons

Tracks and scores correct answers

"Next" and "Exit" buttons

Shows a final result with correct, wrong, and score percentage

# External Files Used:
Mdata.json: Stores questions, options, and correct answers

demo.txt: Stores registered user data (name, parent names, skills, etc.)

# Technologies Used:
Python 3

Tkinter: For GUI design

JSON: For dynamic quiz data

Partial from functools: To pass arguments into Tkinter callbacks

