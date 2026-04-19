
# 🎓 CS50P: Introduction to Programming with Python

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Testing](https://img.shields.io/badge/testing-pytest-yellow.svg)
![Course](https://img.shields.io/badge/course-Harvard_CS50P-red.svg)
![Status](https://img.shields.io/badge/status-Completed-brightgreen.svg)

## 📌 Overview

This repository showcases my progress and project implementations for **Harvard University's CS50P (Introduction to Programming with Python)**. It serves as a comprehensive portfolio demonstrating my transition from basic procedural scripts to advanced, production-ready Python paradigms, including Object-Oriented Programming (OOP), Unit Testing, Regular Expressions, and File I/O.

## 🚀 Weekly Progression & Key Features

The repository is structured chronologically, mapping directly to the course curriculum. Each week highlights a specific programming concept:

* **Week 0: Functions & Variables (`week_0.py`)** * Implementation of a basic Torque Calculator using `input()` and `float()` type conversions.
* **Week 1: Conditionals (`week_1.py`)** * Control flow logic utilizing `if/elif/else` to match user interests with contextual responses.
* **Week 2: Loops (`week_2.py`)** * Data structure iteration. Managing lists of dictionaries to track project statuses and utilizing `while` loops for active countdowns.
* **Week 3: Exceptions (`week_3.py`)** * Defensive programming. Robust user input handling using `try/except` blocks to catch `ValueError`s and prevent runtime crashes.
* **Week 4: Libraries (`week_4.py`)** * Utilizing built-in Python modules like `random` to dynamically select team sprint leaders.
* **Week 5: Unit Tests (`week_5/`)** * Refactoring core logic into testable components. Implemented an automated testing suite using `pytest` to assert positive, negative, and zero-value edge cases.
* **Week 6: File I/O (`week_6.py`)** * Persistent data storage. Automatically logging calculated torque results into a comma-separated values (`torque_log.csv`) file using context managers (`with open()`).
* **Week 7: Regular Expressions (`week_7.py`)** * Advanced data validation. Leveraging the `re` module to strictly validate academic `.edu` email addresses with pattern matching and case insensitivity.
* **Week 8: Object-Oriented Programming (`week_8.py`)** * State and behavior encapsulation. Transitioned from procedural functions to a `Torque` class, utilizing `__init__` constructors and instance methods.
* **Week 9: Et Cetera (`week_9.py`)** * Writing "Pythonic" code. Optimized data formatting using list comprehensions and the `enumerate()` function for clean, readable output.

## ⚙️ Installation & Usage

To run or test the scripts in your local environment, follow these steps:

**1. Clone the repository:**
```bash
git clone [https://github.com/MustafaEnes123/CS50P.git](https://github.com/MustafaEnes123/CS50P.git)
cd CS50P
```

**2. Set up a Virtual Environment & Install Dependencies (Optional but recommended for testing):**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install pytest
```

**3. Run a specific week's script:**
```bash
python week_8.py
```

**4. Execute the automated test suite (Week 5):**
```bash
pytest week_5/test_torque.py
```

## 🛠️ Technologies & Libraries Used

* **Core:** Python 3
* **Testing:** `pytest`
* **Standard Library Modules:** `re`, `random`, `csv`

## 🤝 Acknowledgments

Special thanks to **David J. Malan** and the entire Harvard CS50 team for designing an incredible, challenging, and rewarding curriculum that teaches not just syntax, but the art of algorithmic thinking.

---
*“Coding is not just about writing commands; it’s about structuring data so the machine can think and act logically.”*
