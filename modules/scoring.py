budget_values = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Luxury": 4
}
def calculate_score(destination, selected_region, selected_style,
                    selected_weather, selected_companion,
                    selected_budget, day):

    score = 0

    if selected_region != "Anywhere" and destination["region"] != selected_region:
        return -1

    if destination["region"] == selected_region or selected_region == "Anywhere":
        score = score + 1

    if destination["trip_style"] == selected_style:
        score = score + 1

    if destination["weather"] == selected_weather or selected_weather == "Doesn't Matter":
        score = score + 1

    if budget_values[selected_budget] >= budget_values[destination["budget_level"]]:
        score = score + 1

    if selected_companion in destination["best_for"]:
        score = score + 1

    if day >= destination["min_days"] and day <= destination["max_days"]:
        score = score + 1

    return score