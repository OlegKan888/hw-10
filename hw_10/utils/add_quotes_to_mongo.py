import json
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
db = client.hw


with open('authors.json', 'r', encoding='utf-8') as fd:
    authors = json.load(fd)

for key, author_data in authors.items():
    db.authors.update_one(
        {'fullname': key},
        {"$setOnInsert": {
            'fullname': key,
            'name': author_data.get('name', ''),
            'birth_date': author_data.get('birth_date', ''),
            'birth_place': author_data.get('birth_place', ''),
            'description': author_data.get('description', '')
        }},
        upsert=True
    )


with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for text in quotes:
    author = db.authors.find_one({'fullname': text['author']})
    if author:
        db.quotes.insert_one({
            'text': text['text'],
            'tags': text['tags'],
            'author': ObjectId(author['_id'])
        })
