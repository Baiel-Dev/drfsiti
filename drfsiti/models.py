from django.db import models

class Category(models.Model):  # Добавлено наследование от models.Model
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name


class Women(models.Model):
    title = models.CharField(max_length=255)
    contend = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)  # Ссылка на модель Category

    def __str__(self):
        return self.title
