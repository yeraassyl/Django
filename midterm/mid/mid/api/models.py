from django.db import models
from django.utils import timezone

class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, default="name")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0)
    genre = models.CharField(max_length=255)

class Journal(BookJournalBase):

    TYPE_FIELDS = (
        (1,'Bullet'),
        (2,'Food'),
        (3, 'Travel'),
        (4, 'Sport'),
    )

    type = models.IntegerField(choices=TYPE_FIELDS,default=1)
    publisher = models.CharField(max_length=255)


