# TripMate - Non-Functional Requirements

## NFR-01: Usability

The system should provide a simple and easy-to-understand command-line interface.

The user should be able to enter their preferences by following the displayed options without requiring technical knowledge.


## NFR-02: Maintainability

The system should be organized into separate Python modules based on their responsibilities.

The project separates:

- User input
- Destination data
- Scoring
- Recommendations
- Display

This modular structure makes the project easier to understand, update, and maintain.


## NFR-03: Reliability

The system should consistently produce recommendations based on the user's entered preferences and the predefined destination data.

The same input conditions should produce consistent scoring and ranking results.


## NFR-04: Performance

The system should process the available destination data and generate recommendations within a short amount of time.

The recommendation process should not require significant computational resources.


## NFR-05: Maintainable Data Organization

Destination information should be stored in a structured format so that destinations can be added or modified without changing the main recommendation logic.


## NFR-06: Readability

The Python source code should be organized using meaningful function names, variables, and separate modules so that the program can be understood and modified easily.


## NFR-07: Portability

The application should be able to run on systems that have a compatible Python 3 environment installed, without requiring specialized hardware or software.


## NFR-08: Consistency

The application should present recommendation results in a consistent format, including destination information, match score, recommendation reasons, and the final trip summary.