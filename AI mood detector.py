from textblob import TextBlob # type: ignore

print("👋 Welcome to the AI Mood Detector!")
name = input("What's your name? ")
print(f"Nice to meet you, {name}! Let's find out the sentiment of your sentences.")
print("Type 'exit' anytime to quit.\n")

while True:
    sentence = input("📝 Your sentence: ")
    if sentence.strip().lower() == 'exit':
        print(f"Goodbye, {name}! 👋 Have a great day!")
        break

    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        print("😊 Positive sentiment detected!\n")
    elif sentiment < 0:
        print("😞 Negative sentiment detected!\n")
    else:
        print("😐 Neutral sentiment detected!\n")
