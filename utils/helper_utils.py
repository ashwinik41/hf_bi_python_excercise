import re


def has_chilies(ingredients):
    return bool(re.search(r'\bchil(?:e|i|y|ies?|ly|es)\b', ingredients, re.IGNORECASE))


def get_total_minutes(time_str):
    if not time_str or time_str == "PT":
        return 0
    total_minutes = 0
    time_units = {
        'H': 60,
        'M': 1
    }
    matches = re.findall(r'(\d+)([H|M])', time_str)
    for value, unit in matches:
        total_minutes += int(value) * time_units[unit]
    return total_minutes


def determine_difficulty(prep_time, cook_time):
    total_minutes = get_total_minutes(prep_time) + get_total_minutes(cook_time)
    if total_minutes > 60:
        return "Hard"
    elif 30 <= total_minutes <= 60:
        return "Medium"
    elif total_minutes < 30:
        return "Easy"
    else:
        return "Unknown"


def extract_chilies_recipes(data):
    chilies_recipes = []
    seen_urls = set()
    for recipe in data:
        if recipe.get("url") not in seen_urls and has_chilies(recipe.get("ingredients", "")):
            chilies_recipes.append(recipe)
            seen_urls.add(recipe["url"])
    return chilies_recipes


def calculate_averages(data):
    difficulty_groups = {}
    for recipe in data:
        difficulty = recipe["difficulty"]
        total_time = get_total_minutes(recipe.get("prepTime")) + get_total_minutes(recipe.get("cookTime"))
        if difficulty not in difficulty_groups:
            difficulty_groups[difficulty] = []
        difficulty_groups[difficulty].append(total_time)

    averages = []
    for difficulty, times in difficulty_groups.items():
        average_time = sum(times) // len(times)
        averages.append({"difficulty": difficulty, "average_total_time": average_time})

    return averages
