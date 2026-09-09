# Python Countdown Timer

A simple, interactive Command-Line Interface (CLI) countdown timer built with Python. It accepts a custom message and duration in seconds, displays a real-time formatted countdown (`DD:HH:MM:SS`), and prints your message once the timer completes.

## Features

- **Custom Message & Duration**: Set any text prompt to trigger when time runs out.
- **Formatted Time Display**: Outputs time in `Days:Hours:Minutes:Seconds` format with zero-padded digits.
- **Error Handling**: Uses `try/except` blocks to prevent crashes from non-integer duration inputs.
- **Continuous Loop**: Runs continuously so you can set multiple timers back-to-back.

## How to Run

1. Make sure you have **Python 3** installed on your system.
2. Clone or download this repository.
3. Open your terminal in the project directory and run:

```bash
python3 timer.py
