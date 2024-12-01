from django.db import models


# Модель для авторів
class Author(models.Model):
    name = models.CharField(max_length=100)  # Ім'я автора
    birth_date = models.CharField(max_length=50, null=True, blank=True)  # Дата народження
    birth_place = models.CharField(max_length=150, null=True, blank=True)  # Місце народження
    description = models.TextField(null=True, blank=True)  # Опис

    def __str__(self):
        return self.name


# Модель для тегів
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)  # Назва тегу

    def __str__(self):
        return self.name


# Модель для цитат
class Quote(models.Model):
    text = models.TextField()  # Текст цитати
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="quotes")  # Автор
    tags = models.ManyToManyField(Tag, related_name="quotes")  # Теги

    def __str__(self):
        return self.text[:50]  # Повертає перші 50 символів цитати
