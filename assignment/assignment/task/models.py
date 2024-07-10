from django.db import models

# Create your models here.
class Customer(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name