from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    google_book_id = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=500, null=True)

    def __str__(self):
    	return self.title
