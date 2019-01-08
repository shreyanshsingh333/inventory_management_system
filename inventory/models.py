from django.db import models

# Create your models here.


class Device(models.Model):

    type = models.CharField(max_length=100, blank=False)  # name of the column
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Items ready to be purchased'),
        ('SOLD', 'Items sold'),
        ('RESTOCKING', 'Items restocking in few days')
    )
    status = models.CharField(max_length=10, choices=choices, default="SOLD")  # available, sold, Restocking
    issues = models.CharField(max_length=100, default="No issues")

    # this will stop this class from getting migrated (no table will be
    # created for this class Device
    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0} Price : {1}'.format(self.type, self.price)


# inheritance
class Laptop(Device):
    # you may mention additional fields here
    pass


class Desktop(Device):
    pass


class Mobile(Device):
    pass
