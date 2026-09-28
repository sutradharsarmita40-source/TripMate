# ✈️ TripMate - Your Personal Travel Companion

##  Overview

TripMate is a Python-based travel recommendation system that helps users find suitable travel destinations based on their personal preferences.

The application collects information such as the user's budget, trip duration, preferred region, trip style, weather preference, and travel companion. It then compares these preferences with predefined destination data and calculates a match score for each suitable destination.

The destinations are ranked according to their scores, and the system displays the top three recommendations along with the reasons why they match the user's preferences.

At the end, TripMate provides a personalized trip summary containing the user's selected preferences and the best recommended destination.

##  Objectives

The main objectives of TripMate are:

- To provide a simple travel destination recommendation system.
- To match destinations with user preferences.
- To use Python programming concepts to solve a practical problem.
- To demonstrate modular programming using separate Python files.
- To implement a basic scoring and ranking mechanism.
- To provide understandable explanations for recommendations.
- To generate a personalized trip summary.

##  Features

##  User Information

TripMate collects:

- Name
- Number of travellers
- Trip duration
- Overall budget

## Destination Region

Users can select:

- 🇮🇳 India
- 🌎 International
- 🌍 Anywhere

## Trip Style

Users can choose from:

- Beach
- Mountains
- Nature and Wildlife
- History and Culture
- Adventure
- City and Entertainment
- Relaxation
- Spiritual

## Weather Preference

Users can select:

- Hot
- Pleasant
- Cold
- Snowy
- Doesn't Matter

## Travel Companion

Users can choose:

- Solo
- Friends
- Family
- Partner

## Budget Matching

The entered budget is categorized as:

- Low
- Medium
- High
- Luxury

## Destination Scoring

Each destination is evaluated using:

- Region
- Trip style
- Weather
- Budget
- Travel companion
- Trip duration

A destination can receive a maximum score of **6/6**.

## Ranked Recommendations

The system sorts suitable destinations according to their match scores and displays the top three recommendations.

## Recommendation Explanation

For each recommended destination, TripMate explains matching factors such as:

- Region
- Trip style
- Weather
- Budget
- Travel companion
- Trip duration

## Trip Summary

The final summary displays:

- User name
- Number of travellers
- Duration
- Budget
- Region
- Trip style
- Weather
- Travel companion
- Budget level
- Best recommended destination
- Match score

## Technologies Used

- **Python**
- Python functions
- Conditional statements
- Lists
- Dictionaries
- Loops
- Modules
- Basic sorting
- Basic scoring logic
- Command-line interface
- Git and GitHub

## Project Structure

TripMate/
│
├── main.py
├── README.md
├── statement.md
├── .gitignore
│
└── modules/
    ├── __init__.py
    ├── user_input.py
    ├── destinations.py
    ├── scoring.py
    ├── recommendations.py
    └── display.py

### Module Description

- `main.py` - Main entry point of the TripMate application.
- `modules/user_input.py` - Collects user preferences and basic trip details.
- `modules/destinations.py` - Contains the destination data used by TripMate.
- `modules/scoring.py` - Calculates the match score for destinations.
- `modules/recommendations.py` - Generates and ranks destination recommendations.
- `modules/display.py` - Displays recommendations and the final trip summary.