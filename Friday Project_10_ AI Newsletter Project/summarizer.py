import openai
import os
import time
import logging
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

# Retrieve the API key for OpenAI from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize(text, title="No Title Available"):
    retry_count = 0
    retry_delay = 60  # Start with a 60-second delay
    max_retries = 3

    while retry_count < max_retries:
        try:
            # Request the summary from OpenAI
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

if __name__ == "__main__":
    # Example usage
    article_text = "The Apple M2 iPad Air is now available at its lowest price ever, just in time for the Christmas season. This article discusses its new features and pricing, making it an attractive option for consumers."
    result = summarize(article_text)
    print(result)
