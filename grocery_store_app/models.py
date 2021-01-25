from django.db import models

# Create your models here.


class Customer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email=self.email):
          return True
        return False

    @staticmethod
    def getCustomerByEmail(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def __str__(self):
        return self.fname + self.lname


class Item_data(models.Model):
    key = models.IntegerField(primary_key=True)
    customer = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    item_quantity = models.CharField(max_length=100)
    item_status = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.item_name + self.item_quantity