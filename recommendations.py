from scoring import calculate_score


def get_recommendations(destinations, selected_region, selected_style,
                         selected_weather, selected_companion,
                         selected_budget, day):

    recommendations = []

    for destination in destinations:

        score = calculate_score(
            destination,
            selected_region,
            selected_style,
            selected_weather,
            selected_companion,
            selected_budget,
            day
        )

        if score >= 0:
            recommendations.append({
                "destination": destination,
                "score": score
            })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations