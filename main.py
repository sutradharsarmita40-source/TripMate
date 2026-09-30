from modules.user_input import (
    get_basic_details,
    get_region,
    get_trip_style,
    get_weather,
    get_companion
)

from modules.destinations import destinations
from modules.recommendations import get_recommendations
from modules.display import display_recommendations, display_summary


print("===================================")
print("            TRIPMATE")
print("   YOUR PERSONAL TRAVEL COMPANION")
print("===================================")


nm, tr, day, bd = get_basic_details()

selected_region = get_region()
selected_style = get_trip_style()
selected_weather = get_weather()
selected_companion = get_companion()


if bd <= 15000:
    selected_budget = "Low"
elif bd <= 30000:
    selected_budget = "Medium"
elif bd <= 60000:
    selected_budget = "High"
else:
    selected_budget = "Luxury"


recommendations = get_recommendations(
    destinations,
    selected_region,
    selected_style,
    selected_weather,
    selected_companion,
    selected_budget,
    day
)


display_recommendations(
    recommendations,
    selected_region,
    selected_style,
    selected_weather,
    selected_companion,
    selected_budget,
    day
)


display_summary(
    nm,
    tr,
    day,
    bd,
    selected_region,
    selected_style,
    selected_weather,
    selected_companion,
    selected_budget,
    recommendations
)