# Recipes ETL

This script downloads a JSON file containing recipes, processes the data to extract recipes with "Chilies" as an ingredient, and generates two CSV files: `Chilies.csv` and `Results.csv`.

## Instructions to Run

1. Make sure you have Python installed. 

2. Install the required libraries:
    ```bash
    pip install pandas
    ```
3. Run the script:
    ```bash
    python main.py
    ```
4. To run the unit tests:
    ```bash
    python -m unittest discover -s tests
    ```

## Files

- `main.py`: The main script to process the recipes.
- `Chilies.csv`: CSV file containing recipes with "Chilies".
- `Results.csv`: CSV file containing average total times for each difficulty level.
- `tests/test_main.py`: Unit tests for the script.

## Description

- The script downloads the JSON file from the given URL.
- It extracts recipes that contain "Chilies" (including misspellings like "Chiles" and "Chile").
- It adds a difficulty level to each recipe based on the total time (prepTime + cookTime).
- It writes the filtered recipes to `Chilies.csv`.
- It calculates average total times for each difficulty level and writes to `Results.csv`.
