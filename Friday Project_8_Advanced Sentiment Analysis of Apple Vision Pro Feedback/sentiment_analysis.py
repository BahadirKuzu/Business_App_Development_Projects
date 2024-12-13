import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def analyze_sentiment(review):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Updated to a valid model
            messages=[
                {"role": "system", "content": "You are a sentiment analysis assistant."},
                {"role": "user", "content": f"Analyze the sentiment of this review: {review}"}
            ],
            temperature=0.7
        )
        sentiment = response["choices"][0]["message"]["content"].strip()
        return sentiment
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return "Error"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Error"

        