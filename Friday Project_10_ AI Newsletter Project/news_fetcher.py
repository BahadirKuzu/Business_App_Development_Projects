import requests
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Retrieve the API key for News API
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_news():
    """
    Fetches the top news headlines from the News API and processes the articles.

    Returns:
        List[Tuple[str, str]]: A list of tuples where each tuple contains the title and description of an article.
    """
    if not NEWS_API_KEY:
        logging.error("NEWS_API_KEY not found in environment variables.")
        raise ValueError("NEWS_API_KEY not found in environment variables.")
    
    # Construct the request URL for fetching top headlines in the US
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    
    try:
        # Send the HTTP GET request to the News API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        articles = response.json().get('articles', [])
        
        # Process articles and ensure meaningful descriptions
        processed_articles = []
        for article in articles:
            title = article.get('title', 'No Title Available')  # Fallback title
            description = article.get('description', None)  # Handle missing descriptions
            if description is None or description.strip() == "":
                description = f"This article discusses: {title}"  # Fallback description
            else:
                description = description.strip()  # Clean up the description
            
            processed_articles.append((title, description))
        
        logging.info(f"Fetched and processed {len(processed_articles)} articles.")
        return processed_articles

    except requests.RequestException as e:
        logging.error(f"An error occurred while fetching news: {str(e)}")
        return []

if __name__ == "__main__":
    # Test code to demonstrate functionality
    articles = fetch_news()
    for title, description in articles:
        print(f"Title: {title}")
        print(f"Description: {description}")
        print("-" * 50)
