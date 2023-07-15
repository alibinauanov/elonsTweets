import openai
import key

openai.api_key = key.api_key

tweets = [
    "If your Tesla has >20% charge, Cabin Overheat Protection automatically ensures safety of your loved ones",
    "Future of AI with @elonmusk @rokhanna @mikeforWI",
    "Announcing formation of @xAI to understand reality",
    "Summer 2023 Supercharger voting is now open! Vote for your favorite locations → Tesla Charging",
    "Worth mentioning that you can now watch videos at up to 2X speed and view as pic in pic while still scrolling",
    "You are free to be your true self here",
    "The Outside Context Problem"
]

model_engine = "text-davinci-003"
prompt = "Given a tweet, determine if it is primarily about business or not.\n\nPrint 'yes' if it's about business. I mean Twitter, SpaceX, Tesla."

for tweet in tweets:
    inputText = prompt + f"Tweet: {tweets}\nIs about business? Print 'yes' if it's about business. I mean twitter, spaceX, Tesla."
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=inputText,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    response = completion.choices[0].text
    if "Yes" in response:
        print(1)
    else:
        print(0)