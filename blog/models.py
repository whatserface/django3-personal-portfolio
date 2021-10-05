from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
