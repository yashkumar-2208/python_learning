
# import requests

# API_KEY = "pub_a6577312fa2b41ef9384e54a06305bb3"

# def get_news(country="in", category="technology"):
#     url = "https://newsdata.io/api/1/latest"
#     params = {
#         "apikey": API_KEY,
#         "country": country,
#         "category": category,
#         "language": "en"
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     return data["results"]

# articles = get_news()
# for a in articles:
#     print(a["title"])
#     print(a["link"])
#     print("---")


