import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_sentiment(csv_filename="customer_reviews.csv"):
    """
    Performs basic sentiment analysis on customer reviews and visualizes the results.

    Args:
        csv_filename (str): The name of the CSV file containing reviews.
    """
    try:
        reviews_df = pd.read_csv(csv_filename)
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_filename}' not found. Please run data_generator.py first.")
        return

    # --------------------- Simple Keyword-Based Sentiment Analysis ---------------------
    def get_simple_sentiment(review_text):
        positive_keywords = ["amazing", "happy", "love", "fantastic", "exceeded", "recommended"]
        negative_keywords = ["terrible", "disappointed", "regret", "bad", "not good"]
        neutral_keywords = ["okay", "average", "nothing special", "does the job", "could be better"]

        review_lower = review_text.lower() # Convert to lowercase for case-insensitive matching

        if any(keyword in review_lower for keyword in positive_keywords):
            return "positive"
        elif any(keyword in review_lower for keyword in negative_keywords):
            return "negative"
        else:
            return "neutral"

    reviews_df['predicted_sentiment_simple'] = reviews_df['review_text'].apply(get_simple_sentiment)

    # --------------------- Sentiment Visualization ---------------------
    print("\n--- Sentiment Analysis Results ---")
    print(reviews_df['predicted_sentiment_simple'].value_counts())

    plt.figure(figsize=(8, 6))
    sns.countplot(x='predicted_sentiment_simple', data=reviews_df, order=["positive", "neutral", "negative"])
    plt.title('Distribution of Predicted Sentiments (Simple Keyword Analysis)')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Reviews')
    plt.savefig('sentiment_distribution_simple.png') # Save the plot as an image
    plt.show()


    # --------------------- Rating Distribution Visualization ---------------------
    print("\n--- Rating Distribution ---")
    print(reviews_df['rating'].value_counts().sort_index()) # Sort by rating value

    plt.figure(figsize=(8, 6))
    sns.countplot(x='rating', data=reviews_df, color='skyblue', order=sorted(reviews_df['rating'].unique())) # Ensure ratings are in order
    plt.title('Distribution of Customer Ratings')
    plt.xlabel('Rating (1-5)')
    plt.ylabel('Number of Reviews')
    plt.savefig('rating_distribution.png')
    plt.show()


    print("\n--- Visualizations saved as sentiment_distribution_simple.png and rating_distribution.png ---")

if __name__ == "__main__":
    analyze_sentiment()