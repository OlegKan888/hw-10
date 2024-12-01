import os
import django

from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_10.settings")
django.setup()

from quotes.models import Quote, Tag, Author  # noqa

client = MongoClient("mongodb://localhost")

db = client.hw

authors = db.authors.find()

for author in authors:
    name = author.get("name", None)
    if name is None:
        print(f"Author without a name: {author}")
        continue  # Пропустити записи без імені

    Author.objects.get_or_create(
        name=name,
        birth_date=author.get("birth_date"),
        birth_place=author.get("birth_place"),
        description=author.get("description")
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(name=author['name'])
        q = Quote.object.create(
            quote=quote['quote'],
            author=a
        )

        for tag in tags:
            q.tags.add(tag)
