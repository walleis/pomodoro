PyModoro - Pomodoro Timer
Welcome to PyModoro, a graphical Pomodoro timer built with Python and Tkinter! This application helps you manage your time using the Pomodoro Technique: 25 minutes of focused work followed by short breaks, with a longer break after four cycles. Featuring a tomato-themed GUI, countdown timer, and checkmarks for completed sessions, it’s a great tool for productivity and learning GUI programming.

How It Works
Launch the program to see a window with a tomato image and a timer set to "00:00."
Click "Start" to begin the Pomodoro cycle:
25 minutes of work (green "Work!" label).
5-minute short break (pink "Short Break!" label) after each work session.
20-minute long break (red "Long Break!" label) after four work sessions.
Checkmarks (✔) appear below the timer for each completed work session.
Click "Reset" to stop the timer and clear all progress.
Requirements
Python 3.x: Ensure Python is installed on your system.
Tkinter: Included with standard Python installations for the GUI.
Image File: The program requires tomato.png (a tomato image) in the same directory as the script.
Installation
Download or clone this repository to your computer.
Ensure tomato.png is in the same folder as the script.
Verify Python is installed by running python --version or python3 --version in your terminal.
Run the program by opening a terminal in the project folder and typing:
python pymodoro.py

Features
Implements the Pomodoro Technique with customizable work (25 min), short break (5 min), and long break (20 min) intervals.
Visual feedback with a tomato image and color-coded labels (green for work, pink for short breaks, red for long breaks).
Tracks completed work sessions with checkmarks.
Reset functionality to start over at any time.
Smooth countdown timer updated every second.

Usage Example
Run the program, and a window appears with a tomato and "Timer" label.
Click "Start" → Timer changes to "Work!" and counts down from 25:00.
After 25 minutes, it switches to "Short Break!" for 5 minutes, adding a ✔.
After four work sessions, it switches to "Long Break!" for 20 minutes.
Click "Reset" to return to "00:00" and clear checkmarks.
