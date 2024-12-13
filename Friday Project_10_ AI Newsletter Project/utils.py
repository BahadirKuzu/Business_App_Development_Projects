import openai
import os
import requests
import logging
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# Load environment variables
load_dotenv()

# Load API keys and email credentials
openai.api_key = os.getenv("OPENAI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to fetch news
def fetch_news():
    """
    Fetches the top news headlines from the News API and processes the articles.
    Returns:
        List[Tuple[str, str]]: A list of tuples where each tuple contains the title and description of an article.
    """
    if not NEWS_API_KEY:
        logging.error("NEWS_API_KEY not found in environment variables.")
        raise ValueError("NEWS_API_KEY not found in environment variables.")
    
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        articles = response.json().get('articles', [])
        
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

# Function to summarize text using OpenAI API
def summarize(text, title="No Title Available"):
    retry_count = 0
    retry_delay = 60  # Start with a 60-second delay
    max_retries = 3

    while retry_count < max_retries:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that writes concise summaries."},
                    {"role": "user", "content": f"Provide a detailed but concise summary of the following article. Break it into two short paragraphs, with no more than 200 words in total. Title: {title} \n{text}"}
                ],
                max_tokens=200,  # Limit the length of the summary
                temperature=0.7,  # Optionally adjust temperature for creativity
            )
            
            summary = response.choices[0].message['content']
            
            # Ensure the last sentence is completed properly within the word limit
            if len(summary.split()) > 200:
                summary = " ".join(summary.split()[:200])  # Cut off at the 200 word limit
                if not summary.endswith('.'):
                    summary += '.'  # Add a period if not already there

            return summary
        
        except openai.error.RateLimitError:
            retry_count += 1
            logging.warning(f"Rate limit exceeded. Retrying ({retry_count}/{max_retries})...")
            time.sleep(retry_delay)
            retry_delay *= 2  # Exponential backoff
        
        except openai.error.APIError as e:
            logging.error(f"API error occurred: {str(e)}")
            return f"API error occurred: {str(e)}"
        
        except Exception as e:
            logging.error(f"An unexpected error occurred: {str(e)}")
            return f"An unexpected error occurred: {str(e)}"
    
    return f"Failed to summarize the article titled '{title}' after multiple retries."

# Function to send email
def send_email(subject, body, receiver_email):
    try:
        message = MIMEMultipart()
        message['From'] = EMAIL_USER
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'html'))  # Change to 'html' to support HTML formatting
        
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, receiver_email, message.as_string())
        logging.info(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

