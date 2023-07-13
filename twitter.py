import openai
import key

openai.api_key = key.api_key

company_names = ['AI', 'Twitter', 'SpaceX', 'Tesla']

def evaluate_tweet(tweet):
    keywords = ['AI', 'Twitter', 'SpaceX', 'Tesla']

    for keyword in keywords:
        if keyword.lower() in tweet.lower():
            return 1

    return 0

# Function to process Elon Musk's tweets
def process_elon_tweets(tweets):
    results = []
    for tweet in tweets:
        result = evaluate_tweet(tweet)
        results.append(result)

    return results

elon_tweets = [
    "If your Tesla has >20% charge, Cabin Overheat Protection automatically ensures safety of your loved ones",
    "Future of AI with @elonmusk @rokhanna @mikeforWI",
    "Announcing formation of @xAI to understand reality",
    "Summer 2023 Supercharger voting is now open! Vote for your favorite locations → Tesla Charging",
    "Worth mentioning that you can now watch videos at up to 2X speed and view as pic in pic while still scrolling",
    "You are free to be your true self here",
    "The Outside Context Problem"
]

tweet_results = process_elon_tweets(elon_tweets)

for i, result in enumerate(tweet_results):
    print(f"Tweet {i+1}: {elon_tweets[i]}")
    if result == 1:
        print("Related to a company's business, 1")
    else:
        print("Not related to a company's business, 0")
    print()