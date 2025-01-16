# Ignore environment file
.env
# Ignore Python cache
__pycache__/
*.pyc

# TikTok Search Project

This project uses the TikTok API to search for videos by keywords.

## Setup
1. Clone the repository.
2. Create a `.env` file and add TikTok API key:
3. Install dependencies:
4. Run the script:


import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv("TIKTOK_API_KEY")

# Base URL for TikTok API
BASE_URL = "https://api.tiktok.com/v1/search"

def search_tiktok(query, max_results=10):
    """
    Function to search TikTok videos using the TikTok API.

    Args:
        query (str): The search keyword or phrase.
        max_results (int): Maximum number of results to fetch (default is 10).

    Returns:
        dict: The search results in JSON format.
    """
    if not API_KEY:
        print("Error: API Key not found. Please set it in the .env file.")
        return None

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    params = {
        "query": query,
        "limit": max_results
    }

    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    # Input from the user
    search_query = input("Enter your search query: ")
    max_results = int(input("Enter the maximum number of results to fetch: "))

    # Perform search
    results = search_tiktok(search_query, max_results)

    if results:
        print("Search Results:")
        for result in results.get("data", []):
            print(f"Title: {result['title']}, URL: {result['url']}")
    else:
        print("No results found or an error occurred.")

