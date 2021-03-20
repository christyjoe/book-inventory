from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    google_book_id = models.IntegerField(default=0)

    def __str__(self):
    	return self.title
