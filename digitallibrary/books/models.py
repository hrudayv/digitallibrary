from django.db import models

# Create your models here.
class book(models.Model):
    bookname = models.CharField(max_length=100)
    authorname = models.CharField(max_length=200)
    booknum = models.IntegerField()
    stockavail = models.IntegerField()
    noc = models.IntegerField(default=0)

    def __str__(self):
        return self.bookname + " - " + self.authorname
