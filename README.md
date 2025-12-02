
# 📌 Add these keys to your .env:

API_BASE_URL=https://api.example.com

API_TOKEN=abcd12

API_PATH=/v1/users

OUTPUT_FILE=users.csv


DATA_KEY=data

NEXT_PAGE_KEY=next_page


# If your API uses another structure, just update .env:

# #Example 1 — GitHub style
DATA_KEY=items
NEXT_PAGE_KEY=next

## Example 2 — Google-style tokens
NEXT_PAGE_KEY=nextPageToken
DATA_KEY=documents

## Example 3 — Custom API
DATA_KEY=data
NEXT_PAGE_KEY=next_page
