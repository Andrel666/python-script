import os
import csv
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_BASE_URL")
API_TOKEN = os.getenv("API_TOKEN")
API_PATH = os.getenv("API_PATH", "/v1/items")
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "data.csv")

# 👇 NEW: Key where the API returns pagination pointer
NEXT_PAGE_KEY = os.getenv("NEXT_PAGE_KEY", "next_page")

# 👇 NEW: Key where the API returns the list of items
DATA_KEY = os.getenv("DATA_KEY", "data")

def fetch_all():
    url = f"{BASE_URL.rstrip('/')}/{API_PATH.lstrip('/')}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    params = {}

    all_items = []
    next_page_value = None

    while True:
        # Apply pagination if provided
        if next_page_value:
            params["page"] = next_page_value

        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        payload = response.json()

        # Fetch items using data key (generic)
        items = payload.get(DATA_KEY, [])
        all_items.extend(items)

        # Read pagination key dynamically (generic)
        next_page_value = payload.get(NEXT_PAGE_KEY)

        if not next_page_value:
            break

    return all_items


def write_csv(rows, path):
    if not rows:
        print("No data retrieved.")
        return

    fieldnames = sorted(rows[0].keys())

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    data = fetch_all()
    write_csv(data, OUTPUT_FILE)
    print(f"Retrieved {len(data)} items and saved to {OUTPUT_FILE}")
