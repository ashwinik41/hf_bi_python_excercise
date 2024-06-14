from utils.file_utils import download_json, read_json, save_to_csv
from utils.helper_utils import extract_chilies_recipes, determine_difficulty, calculate_averages


def main():
    recipes_file_url = "https://bnlf-tests.s3.eu-central-1.amazonaws.com/recipes.json"
    json_filename = "bi_recipes.json"
    base_directory = "recipes-etl"
    chilies_filename = "Chilies.csv"
    results_filename = "Results.csv"

    download_json(recipes_file_url, json_filename)

    recipes_data = read_json(json_filename)

    # Extract recipes with "Chilies" in ingredients
    chilies_recipes = extract_chilies_recipes(recipes_data)

    # Determine difficulty for each recipe
    for recipe in chilies_recipes:
        recipe["difficulty"] = determine_difficulty(recipe.get("prepTime"), recipe.get("cookTime"))

    # Save extracted recipes to Chilies.csv
    save_to_csv(chilies_recipes, base_directory, chilies_filename)

    # Calculate averages and save to Results.csv
    averages = calculate_averages(chilies_recipes)
    save_to_csv(averages, base_directory, results_filename)
    print(f"done processing {json_filename}")


if __name__ == "__main__":
    main()
