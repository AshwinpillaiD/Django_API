from django.db import models

# Create your models here.


class category(models.Model):
    category=models.CharField(max_length=254,null=True)

    def __str__(self):
        return self.category



class Products(models.Model):

    category_ref=models.ForeignKey(category,null=True, on_delete=models.SET_NULL)
    products=models.CharField(max_length=254,null=True)
    code=models.CharField(max_length=50,null=True)
    price=models.FloatField(null=True,default=0)

    def __str__(self):
        return self.products