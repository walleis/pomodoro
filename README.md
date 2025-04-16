# PyModoro - A Pomodoro Timer Application

## Description

PyModoro is a simple and visually appealing Pomodoro timer application built using Python's Tkinter library. The Pomodoro Technique is a time management method that breaks work into focused intervals, traditionally 25 minutes in length, separated by short breaks (typically 5 minutes), with a longer break (usually 20 minutes) after every four work intervals. This application helps you follow this technique to improve focus and productivity.

## How to Use

1.  **Run the script:** Execute the Python script. A window titled "PyModoro" will appear, featuring a tomato image and an initial timer set to "00:00".
2.  **Start the timer:** Click the "Start" button. The timer will begin a 25-minute work session. The title of the timer label will change to "Work!", and the color will turn green.
3.  **Work session:** Focus on your task until the timer reaches 00:00.
4.  **Short break:** Once the work session ends, a 5-minute short break will automatically start. The timer label will change to "Short Break!" and turn pink. A checkmark (✔) will also appear below the timer to track completed work sessions.
5.  **Continue the cycle:** After the short break, another 25-minute work session will begin, followed by another short break.
6.  **Long break:** After every four work sessions, a longer 20-minute break will automatically start. The timer label will change to "Long Break!" and turn red.
7.  **Track progress:** Checkmarks will accumulate below the timer after each completed work session, helping you visualize your progress.
8.  **Reset the timer:** If you need to stop or restart the Pomodoro cycle, click the "Reset" button. This will stop the current timer, reset the countdown to "00:00", change the timer label back to "Timer" (in green), and clear the checkmarks.
9.  **Close the application:** You can close the application window when you are finished with your work sessions.

## Functionality

* **Pomodoro Timer:** Implements the core Pomodoro Technique with customizable work, short break, and long break durations (default: 25 min work, 5 min short break, 20 min long break).
* **Visual Feedback:** Provides clear visual cues through color changes and text updates to indicate the current phase (Work!, Short Break!, Long Break!).
* **Countdown Display:** Shows the remaining time in minutes and seconds, updating every second.
* **Work Session Tracking:** Displays checkmarks to track the number of completed work sessions, indicating when it's time for a long break.
* **Start and Reset Controls:** Offers "Start" and "Reset" buttons for easy control of the timer.
* **Customizable Appearance:** Uses specific colors (PINK, RED, GREEN, YELLOW) and a font (Courier) to create a distinctive look.

## Requirements

* Python 3.x (The `tkinter` and `math` modules are typically included with standard Python installations.)
* A `tomato.png` image file in the same directory as the script. This image is used as a visual element in the timer window.

## Installation

1.  Ensure you have Python installed on your system.
2.  Download a `tomato.png` image and save it in the same directory where you will save the Python script.
3.  Save the provided code as a `.py` file (e.g., `pomodoro_timer.py`).
4.  Run the script using a Python interpreter:
    ```bash
    python pymodoro.py
    ```

## Code Explanation

* **Color and Font Definitions:** Defines color codes (PINK, RED, GREEN, YELLOW) and the font name (FONT\_NAME) for styling the GUI elements.
* **Timer Durations:** Sets the default work, short break, and long break durations in minutes (WORK\_MIN, SHORT\_BREAK\_MIN, LONG\_BREAK\_MIN).
* **`reps` Variable:** A global variable to keep track of the number of Pomodoro cycles (work + break) completed.
* **`timer` Variable:** A global variable to store the `after` method's return value, allowing the timer to be stopped.
* **`reset_timer()` Function:**
    * Cancels any ongoing timer using `window.after_cancel(timer)`.
    * Resets the timer display on the canvas to "00:00".
    * Resets the timer label text to "Timer" and its color to green.
    * Clears the checkmark label.
    * Resets the global `reps` counter to 0.
* **`start_timer()` Function:**
    * Increments the global `reps` counter.
    * Calculates the work, short break, and long break durations in seconds.
    * Uses conditional logic based on the `reps` count to determine whether to start a long break (after 8 reps), a short break (after every other rep), or a work session.
    * Calls the `countdown()` function with the appropriate duration in seconds and updates the timer label text and color accordingly.
* **`countdown(count)` Function:**
    * Takes the remaining `count` in seconds as input.
    * Calculates the remaining minutes and seconds.
    * Formats the seconds to always have two digits (e.g., "05" instead of "5").
    * Updates the timer text on the canvas using `canvas.itemconfig()`.
    * If `count` is greater than 0, it schedules the `countdown()` function to be called again after 1000 milliseconds (1 second) with `count - 1`, storing the ID in the global `timer` variable.
    * If `count` reaches 0:
        * It calls `start_timer()` to begin the next session (break or work).
        * It updates the checkmark label by adding a "✔" for every two completed reps (representing a completed work session).
* **Window Setup:**
    * Creates the main window (`window = Tk()`).
    * Sets the window title to "PyModoro".
    * Configures padding and background color for the window.
* **Canvas Setup:**
    * Creates a `Canvas` widget with a specified width and height and sets its background color.
    * Loads the `tomato.png` image using `PhotoImage()`.
    * Creates an image on the canvas using the loaded tomato image.
    * Creates text on the canvas to display the timer countdown, initially set to "00:00", with white color and a bold Courier font.
    * Places the canvas in the grid layout.
* **Labels:**
    * Creates the "Timer" label with specified font, background color, and initial foreground color (green).
    * Places the timer label in the grid layout.
    * Creates the checkmark label with the window's background color.
    * Places the checkmark label in the grid layout.
* **Buttons:**
    * Creates the "Start" button and associates it with the `start_timer()` function using the `command` argument.
    * Places the start button in the grid layout.
    * Creates the "Reset" button and associates it with the `reset_timer()` function.
    * Places the reset button in the grid layout.
* **`window.mainloop()`:** Starts the Tkinter event loop, making the GUI interactive and responsive to events (like button clicks and timer updates).
