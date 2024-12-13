import sqlite3
import pandas as pd
from sentiment_analysis import analyze_sentiment
from data_visualization import visualize_data

# Connect to the database
conn = sqlite3.connect("feedback.db")

# Fetch data from the database
reviews_df = pd.read_sql_query("SELECT * FROM reviews", conn)

# Perform sentiment analysis
reviews_df["sentiment"] = reviews_df["review"].apply(analyze_sentiment)

# Visualize the results
visualize_data(reviews_df)

# Save the results back to the database
reviews_df.to_sql("reviews", conn, if_exists="replace", index=False)

print("Analysis completed and results saved!")
conn.close()
