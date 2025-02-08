import csv
import random

def generate_reviews_csv(filename="customer_reviews.csv", num_reviews=1000):
    """
    Generates a CSV file with simulated customer reviews.

    Args:
        filename (str): The name of the CSV file to create.
        num_reviews (int): The number of reviews to generate.
    """
    reviews = []
    sentiments = ["positive", "negative", "neutral"]
    products = ["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch"]
    review_templates = [
        "The {product} is amazing! I love it.",
        "I'm very happy with my new {product}.",
        "This {product} is okay, nothing special.",
        "The {product} is not bad, but could be better.",
        "I'm a bit disappointed with this {product}.",
        "The {product} is terrible! Don't buy it.",
        "I regret buying this {product}.",
        "This {product} exceeded my expectations.",
        "It's an average {product}, does the job.",
        "This {product} is fantastic, highly recommended!"
    ]

    for i in range(num_reviews):
        sentiment = random.choice(sentiments)
        product = random.choice(products)
        review_text = random.choice(review_templates).format(product=product)
        rating = random.randint(1, 5) # Simulate ratings from 1 to 5
        reviews.append([review_text, sentiment, rating])

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["review_text", "sentiment", "rating"]) # Header row
        csv_writer.writerows(reviews)

    print(f"Generated {num_reviews} simulated reviews in '{filename}'")

if __name__ == "__main__":
    generate_reviews_csv(num_reviews=1000) # Generate 1000 reviews