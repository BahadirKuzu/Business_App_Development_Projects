import matplotlib.pyplot as plt

def visualize_data(reviews_df):
    sentiment_counts = reviews_df["sentiment"].value_counts()
    sentiment_counts.plot(kind="bar", color="blue", alpha=0.7)
    plt.title("Sentiment Analysis of Reviews")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Reviews")
    plt.show()
