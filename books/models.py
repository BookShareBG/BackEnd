from django.db import models


class Book(models.Model):
    isbn = models.TextField(unique=True)

    title = models.TextField()
    author = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'
