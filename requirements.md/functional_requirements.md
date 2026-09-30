# TripMate - Functional Requirements

## FR-01: Collect Basic Trip Information

The system shall allow the user to enter their basic travel information, including:

- Name
- Number of travellers
- Planned trip duration
- Overall travel budget

The system shall use this information while generating travel recommendations.


## FR-02: Select Destination Region

The system shall allow the user to select their preferred destination region from:

1. India
2. International
3. Anywhere

If the user selects India, only destinations belonging to India shall be considered.

If the user selects International, only international destinations shall be considered.

If the user selects Anywhere, destinations from both regions shall be considered.


## FR-03: Select Trip Style

The system shall allow the user to select a preferred trip style from:

- Beach
- Mountains
- Nature and Wildlife
- History and Culture
- Adventure
- City and Entertainment
- Relaxation
- Spiritual

The selected trip style shall be used as one of the criteria for destination matching.


## FR-04: Select Weather Preference

The system shall allow the user to select a preferred weather condition from:

- Hot
- Pleasant
- Cold
- Snowy
- Doesn't Matter

The selected weather preference shall be compared with the weather information stored for each destination.


## FR-05: Select Travel Companion

The system shall allow the user to specify their travel companion:

- Solo
- Friends
- Family
- Partner

The system shall use the selected companion while evaluating destination suitability.


## FR-06: Determine Budget Level

The system shall categorize the user's entered budget into one of four levels:

- Low
- Medium
- High
- Luxury

The budget level shall be compared with the budget level associated with each destination.


## FR-07: Filter Destinations

The system shall filter destinations according to the selected region.

Destinations that do not belong to the selected region shall not be considered for the final recommendations.

When the user selects "Anywhere", destinations from both India and International categories may be considered.


## FR-08: Calculate Destination Match Score

The system shall calculate a match score for each suitable destination.

The score shall consider six criteria:

1. Region
2. Trip style
3. Weather
4. Budget
5. Travel companion
6. Trip duration

Each satisfied criterion shall contribute to the destination's total score.

The maximum possible match score shall be 6.


## FR-09: Rank Destinations

The system shall sort suitable destinations according to their calculated match scores in descending order.

Destinations with higher match scores shall appear before destinations with lower match scores.


## FR-10: Display Top Recommendations

The system shall display the top three recommended destinations.

For each recommendation, the system shall display:

- Destination name
- Match score
- Trip style
- Weather
- Budget level
- Suitable travel companions
- Ideal duration
- Activities


## FR-11: Explain Recommendations

The system shall display the factors that caused a destination to be recommended.

The explanation may include:

- Region match
- Trip style match
- Weather match
- Budget compatibility
- Travel companion suitability
- Trip duration compatibility


## FR-12: Display Best Destination

The system shall identify the highest-ranked destination as the best recommended destination.

The system shall display:

- Best destination name
- Match score


## FR-13: Generate Trip Summary

The system shall display a final trip summary containing:

- User name
- Number of travellers
- Trip duration
- Budget
- Destination region
- Trip style
- Weather preference
- Travel companion
- Budget level
- Best recommended destination
- Match score