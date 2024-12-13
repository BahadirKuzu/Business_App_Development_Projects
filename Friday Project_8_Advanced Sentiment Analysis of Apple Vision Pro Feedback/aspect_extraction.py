import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def extract_aspects(review):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using gpt-3.5-turbo
            messages=[
                {"role": "system", "content": "You are an aspect extraction assistant."},
                {"role": "user", "content": f"Extract aspects from this review: {review}"}
            ]
        )
        aspects = response['choices'][0]['message']['content'].strip()
        return aspects
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        return "Error"
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return "Error"

# Test function
if __name__ == "__main__":
    review = "The product quality is excellent, but the delivery was delayed."
    extracted_aspects = extract_aspects(review)
    print("Extracted Aspects:", extracted_aspects)
  
  