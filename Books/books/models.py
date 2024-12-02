from django.db import models


class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'В наличии'),
        ('issued', 'Выдана'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.title} ({self.author})"