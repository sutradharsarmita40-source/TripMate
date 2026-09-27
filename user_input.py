def get_basic_details():
    nm = input("What is your name? ")
    tr = int(input("How many travellers are there? "))
    day = int(input("How many days are you planning to travel? "))
    bd = int(input("What is your overall budget? ₹"))

    return nm, tr, day, bd


def get_region():

    print("===================================")
    print("      WHERE DO YOU WANT TO GO?")
    print("===================================")

    print("1. India")
    print("2. International")
    print("3. Anywhere")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        selected_region = "India"
    elif ch == 2:
        selected_region = "International"
    elif ch == 3:
        selected_region = "Anywhere"
    else:
        selected_region = "Invalid"

    return selected_region

def get_trip_style():

    print("===================================")
    print("      CHOOSE YOUR TRIP STYLE")
    print("===================================")

    print("1. BEACH")
    print("2. MOUNTAINS")
    print("3. NATURE AND WILDLIFE")
    print("4. HISTORY AND CULTURE")
    print("5. ADVENTURE")
    print("6. CITY AND ENTERTAINMENT")
    print("7. RELAXATION")
    print("8. SPIRITUAL")

    style = int(input("Enter your choice: "))

    if style == 1:
        selected_style = "Beach"
    elif style == 2:
        selected_style = "Mountains"
    elif style == 3:
        selected_style = "Nature and Wildlife"
    elif style == 4:
        selected_style = "History and Culture"
    elif style == 5:
        selected_style = "Adventure"
    elif style == 6:
        selected_style = "City and Entertainment"
    elif style == 7:
        selected_style = "Relaxation"
    elif style == 8:
        selected_style = "Spiritual"
    else:
        selected_style = "Invalid"

    return selected_style

def get_weather():

    print("===================================")
    print("        WEATHER PREFERENCE")
    print("===================================")

    print("1. HOT")
    print("2. PLEASANT")
    print("3. COLD")
    print("4. SNOWY")
    print("5. DOESN'T MATTER")

    wt = int(input("Enter your choice: "))

    if wt == 1:
        selected_weather = "Hot"
    elif wt == 2:
        selected_weather = "Pleasant"
    elif wt == 3:
        selected_weather = "Cold"
    elif wt == 4:
        selected_weather = "Snowy"
    elif wt == 5:
        selected_weather = "Doesn't Matter"
    else:
        selected_weather = "Invalid"

    return selected_weather

def get_companion():

    print("====================================")
    print("    CHOOSE YOUR TRAVEL COMPANION")
    print("====================================")

    print("1. SOLO")
    print("2. FRIENDS")
    print("3. FAMILY")
    print("4. PARTNER")

    com = int(input("Enter your choice: "))

    if com == 1:
        selected_companion = "Solo"
    elif com == 2:
        selected_companion = "Friends"
    elif com == 3:
        selected_companion = "Family"
    elif com == 4:
        selected_companion = "Partner"
    else:
        selected_companion = "Invalid"

    return selected_companion