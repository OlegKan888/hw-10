from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),  # Головна сторінка
    path("page/<int:page>/", views.main, name="paginated"),  # Сторінки з пагінацією
]
