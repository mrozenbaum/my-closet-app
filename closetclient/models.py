from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    """Adds a Category model to our SQLite database."""
    category_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date added')

    # returns human readable string
    def __str__(self): # only if you need to support Python 2
        return self.category_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)        


class Item(models.Model):
    """Adds an Item model to our SQLite database."""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    item_count = models.IntegerField(default=0)

    # returns human readable string
    def __str__(self): # only if you need to support Python 2
        return self.item_name




    

