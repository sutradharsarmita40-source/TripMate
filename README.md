# TripMate – Your Personal Travel Companion

## 1. Project Overview

TripMate is a Python-based travel recommendation system that helps users find suitable travel destinations based on their personal preferences.

The user provides basic details such as their name, trip duration, budget, preferred region, trip style, weather preference, and travel companion. TripMate processes these preferences and recommends destinations that match the user's requirements.

The project is developed as a beginner-friendly Python application using fundamental Python concepts such as variables, data types, conditional statements, loops, lists, dictionaries, functions, and modules.

---

## 2. Features

* Collects basic information from the user.
* Allows users to select a travel region:

  * India
  * International
  * Anywhere
* Allows users to select their preferred trip style:

  * Beach
  * Mountains
  * Nature and Wildlife
  * History and Culture
  * Adventure
  * City and Entertainment
  * Relaxation
  * Spiritual
* Allows users to select their preferred weather:

  * Hot
  * Pleasant
  * Cold
  * Snowy
  * Doesn't Matter
* Allows users to select their travel companion:

  * Solo
  * Friends
  * Family
  * Partner
* Categorizes the user's budget into different levels.
* Matches user preferences with available destinations.
* Displays recommended destinations.
* Displays the best matching destination.
* Displays a summary of the user's trip preferences.
* Uses separate Python modules to organize the project.

---

## 3. Technologies and Tools Used

### Programming Language

* Python

### Concepts Used

* Variables
* Data Types
* Conditional Statements
* Loops
* Lists
* Dictionaries
* Functions
* Modules
* Basic input and output

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## 4. Project Structure

```text
TripMate/
│
├── main.py
│
├── modules/
│   ├── user_input.py
│   ├── destinations.py
│   ├── recommendations.py
│   └── display.py
│
├── requirements.md/
│   ├── functional_requirements.md
│   └── non_functional_requirements.md
│
├── README.md
└── statement.md
```

### Description of Modules

**main.py**
Controls the overall flow of the application and connects all modules.

**user_input.py**
Contains functions that collect the user's travel preferences.

**destinations.py**
Contains the destination data used by TripMate.

**recommendations.py**
Processes the user's preferences and generates suitable destination recommendations.

**display.py**
Displays the recommendations and trip summary in a user-friendly format.

---

## 5. Installation and Setup

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation using:

```bash
python3 --version
```

### Step 2: Clone the Repository

Clone the TripMate GitHub repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### Step 3: Open the Project

Open the downloaded project folder in Visual Studio Code or any Python-supported editor.

### Step 4: Run the Project

Open the terminal inside the project folder and run:

```bash
python3 main.py
```

---

## 6. How to Use the Application

1. Run `main.py`.
2. Enter your basic trip details.
3. Select your preferred region.
4. Select your preferred trip style.
5. Select your preferred weather.
6. Select your travel companion.
7. Enter your budget.
8. TripMate processes the selected preferences.
9. The application displays suitable destination recommendations.
10. The best matching destination and trip summary are displayed.

---

## 7. Testing Instructions

The application can be tested by providing different combinations of user inputs.

### Test Case 1 – India

* Region: India
* Trip Style: Mountains
* Weather: Cold
* Companion: Friends
* Budget: Medium

**Expected Result:**
The application should display suitable Indian destinations matching these preferences.

### Test Case 2 – International

* Region: International
* Trip Style: Mountains
* Weather: Snowy
* Companion: Partner
* Budget: High

**Expected Result:**
The application should display suitable international beach destinations.

### Test Case 3 – Anywhere

* Region: Anywhere
* Trip Style: Beach
* Weather: Doesn't matter
* Companion: Friends
* Budget: Medium

**Expected Result:**
The application should search across the available destinations and display suitable recommendations.

### Test Case 4 – Different Budget

Test the application with different budget values to verify that the budget category is correctly identified.

The application should classify the budget into the appropriate category based on the entered amount.

---

## 8. Project Objective

The main objective of TripMate is to demonstrate how fundamental Python programming concepts can be combined to create a useful travel recommendation application.

The project also demonstrates modular programming by separating user input, destination data, recommendation logic, and output display into different Python files.

---

## 9. Future Enhancements

Possible future improvements include:

* Adding more destinations.
* Adding more detailed destination information.
* Adding estimated travel costs.
* Adding accommodation suggestions.
* Adding weather information through an API.
* Creating a graphical or web-based interface.
* Adding more personalized recommendation criteria.

---

## 10. Conclusion

TripMate is a simple Python-based travel companion that helps users explore destinations according to their preferences. The project demonstrates the practical use of Python fundamentals, functions, dictionaries, lists, conditional statements, loops, and modules in a real-world application.
