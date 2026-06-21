import json
import random
import requests

URL = "https://openlibrary.org/search.json"

collections = [
    "Классика",
    "Фэнтези",
    "Детективы",
    "Научная фантастика",
    "Романы",
    "Приключения"
]

categories = ["0+", "6+", "12+", "16+", "18+"]
publishers_default = ["АСТ", "Эксмо", "Азбука", "Росмэн", "Питер"]

params = {
    "q": "classic literature",
    "limit": 100,
    "language": "rus"
}

response = requests.get(URL, params=params, timeout=20)
response.raise_for_status()

data = response.json()
books = []

for index, item in enumerate(data.get("docs", [])[:100], start=1):
    title = item.get("title") or f"Книга {index}"

    authors = item.get("author_name") or ["Автор не указан"]
    author = authors[0]

    publishers = item.get("publisher") or publishers_default
    publisher = publishers[0]

    year = item.get("first_publish_year") or random.randint(1950, 2024)

    cover_id = item.get("cover_i")
    cover = None

    if cover_id:
        cover = f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg"

    book = {
        "title": title,
        "author": author,
        "description": "Описание книги загружено из моковых данных Open Library.",
        "cover": cover,
        "publisher": publisher,
        "category": random.choice(categories),
        "year": year,
        "collection": random.choice(collections),
        "is_available": random.choice([True, True, True, False]),
        "is_favorite": False,
        "is_reserved": False
    }

    books.append(book)

with open("seed_books.json", "w", encoding="utf-8") as file:
    json.dump(books, file, ensure_ascii=False, indent=2)

print(f"Создан файл seed_books.json. Количество книг: {len(books)}")