# AI-Powered News Newsletter

## Project Overview

The AI-Powered News Newsletter project automates the process of fetching the latest news articles, summarizing them, and delivering the summaries via email. It utilizes OpenAI's GPT-3.5 model for generating concise summaries, and integrates with the News API to fetch the top news articles. This project can be scheduled to run daily, ensuring that users receive the latest news in an email-friendly format without the need for manual effort.

## Features

- **Fetches Latest News**: Uses the [News API](https://newsapi.org/) to get the latest news headlines from various reliable sources.
- **Summarization**: Leverages OpenAI’s GPT-3.5 to summarize news articles into concise, email-friendly summaries.
- **Automated Email Delivery**: Sends the summarized news articles directly to the user’s email address, making it easy to stay updated.
- **Environment Variables**: Uses `.env` for securely storing API keys and email credentials.

## Prerequisites

- Python 3.6 or higher
- Access to the following APIs:
  - [OpenAI API Key](https://beta.openai.com/signup/)
  - [News API Key](https://newsapi.org/register)
- A Gmail account or an SMTP server to send emails.

## Installation

1. **Clone this repository** to your local machine:

   ```bash
   git clone https://github.com/yourusername/AI_Newsletter_Project.git

2. **Navigate to the project directory** and install the required Python dependencies:

   cd AI_Newsletter_Project
   pip install -r requirements.txt

3. **Create a .env file** in the root directory of the project with the following contents (replace with your actual credentials):

# AI-Powered News Newsletter

## Installation and Usage

```
# Clone this repository
git clone https://github.com/yourusername/AI_Newsletter_Project.git

# Navigate to the project directory
cd AI_Newsletter_Project

# Install the required Python dependencies
pip install -r requirements.txt

# Create a .env file in the root directory with your credentials
OPENAI_API_KEY="your_openai_api_key_here"
NEWS_API_KEY="your_news_api_key_here"
EMAIL_USER="your_email@gmail.com"
EMAIL_PASSWORD="your_email_password"
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=587

# Run the project
python main.py

# Schedule the script to run daily using cron or Task Scheduler
```

## Testing

This project includes unit tests for critical functionalities such as sending emails and fetching news. To run the tests, use the following command:

```bash
python -m unittest tests/test_email_sender.py
```

Make sure the necessary credentials and environment variables are set up before running the tests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Feel free to fork this repository, open issues, and submit pull requests. All contributions are welcome!

