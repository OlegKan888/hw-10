from bson import ObjectId
from django.shortcuts import render
from django.core.paginator import Paginator
from .utils import get_mongodb


def main(request):
    db = get_mongodb()
    quotes_list = list(db.quotes.find())

    # Додаємо імена авторів до цитат
    for quote in quotes_list:
        author_id = quote.get("author")
        author = db.authors.find_one({"_id": ObjectId(author_id)})
        quote["author_name"] = author.get("fullname") if author else "Unknown Author"

    # Пагінація
    page = request.GET.get("page", 1)  # Отримуємо номер сторінки з GET-запиту
    per_page = 10
    paginator = Paginator(quotes_list, per_page)
    quotes = paginator.get_page(page)

    return render(request, "quotes/index.html", context={"quotes": quotes})
