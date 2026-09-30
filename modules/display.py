def display_recommendations(recommendations, selected_region,
                            selected_style, selected_weather,
                            selected_companion, selected_budget, day):

    budget_values = {
        "Low": 1,
        "Medium": 2,
        "High": 3,
        "Luxury": 4
    }

    print()
    print("===================================")
    print("        TRIPMATE RESULTS")
    print("===================================")

    rank = 1

    for recommendation in recommendations[:3]:

        destination = recommendation["destination"]
        score = recommendation["score"]

        print()

        if rank == 1:
            print("1.",destination["name"])
        elif rank == 2:
            print("2.",destination["name"])
        else:
            print("3.",destination["name"])

        print("Match Score:", score, "/ 6")
        print("Trip Style:", destination["trip_style"])
        print("Weather:", destination["weather"])
        print("Budget Level:", destination["budget_level"])
        print("Best For:", destination["best_for"])
        print("Ideal Duration:", destination["min_days"], "-", destination["max_days"], "days")
        print("Activities:", destination["activities"])

        print()
        print("Why we recommend it:")

        if destination["region"] == selected_region or selected_region == "Anywhere":
            print("✓ Matches your region")

        if destination["trip_style"] == selected_style:
            print("✓ Matches your trip style")

        if destination["weather"] == selected_weather or selected_weather == "Doesn't Matter":
            print("✓ Matches your weather preference")

        if budget_values[selected_budget] >= budget_values[destination["budget_level"]]:
            print("✓ Fits your budget")

        if selected_companion in destination["best_for"]:
            print("✓ Suitable for your companion")

        if day >= destination["min_days"] and day <= destination["max_days"]:
            print("✓ Fits your trip duration")

        print("-----------------------------------")

        rank = rank + 1
       

def display_summary(nm, tr, day, bd, selected_region,
                   selected_style, selected_weather,
                   selected_companion, selected_budget,
                   recommendations):

    best_destination = recommendations[0]["destination"]
    best_score = recommendations[0]["score"]

    print()
    print("===================================")
    print("         YOUR TRIP SUMMARY")
    print("===================================")

    print("Name:", nm)
    print("Travellers:", tr)
    print("Duration:", day, "days")
    print("Budget:", "₹", bd)
    print("Destination Region:", selected_region)
    print("Trip Style:", selected_style)
    print("Weather:", selected_weather)
    print("Travel Companion:", selected_companion)
    print("Budget Level:", selected_budget)

    print()
    print("Best Recommended Destination:", best_destination["name"])
    print("Match Score:", best_score, "/ 6")

    print("===================================")
    print("       THANK YOU FOR USING")
    print("             TRIPMATE")
    print("===================================")