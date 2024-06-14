import json
import os
import urllib

import pandas as pd


def download_json(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded {filename} successfully.")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")


def read_json(filename):
    try:
        data = []
        with open(filename, 'r') as file:
            for line in file:
                data.append(json.loads(line))
        return data
    except Exception as e:
        print(f"Failed to read {filename}: {e}")
        return []


def save_to_csv(data, dir, filename):
    # Create directory if it doesn't exist
    directory = dir
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save to CSV
    df = pd.DataFrame(data)
    filepath = os.path.join(directory, filename)
    df.to_csv(filepath, sep='|', index=False)
    print(f"Saved {filename} successfully.")
