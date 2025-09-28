import requests
from apis import NEWS_API_KEY

def get_news(speak):
    url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-06-20&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        articles = response.json().get("articles", [])[:5]
        if articles:
            speak("Here are the top headlines.")
            for article in articles:
                speak(article["title"])
                print(article["title"])
        else:
            speak("No news found.")
    except Exception as e:
        print(e)
        speak("Unable to fetch news at the moment.")
