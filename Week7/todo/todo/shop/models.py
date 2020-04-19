from django.db import models
from todo.auth_.models import MyUser
from datetime import datetime

class CategoryManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class ProductManager(models.Manager):
    pass



class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    objects = CategoryManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    @property
    def short_name(self):
        return self.name[:10]

    @classmethod
    def count(cls):
        return cls.objects.count()


class ProductBase(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(default = datetime.now)
    price = models.IntegerField(default=0, null=False)

    objects = ProductManager()

    class Meta:
        abstract=True


class OnlineProduct(ProductBase):
    status = models.CharField(max_length=255)
    sale = models.CharField(max_length=255)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ('name',)

    @property
    def short_name(self):
        return self.name[:5]

    @classmethod
    def count(cls):
        return cls.objects.count()

class OfflineProduct(ProductBase):
    pass