from django.db import models

# Create your models here.

class Weight(models.Model):
    weight_range = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.weight_range} / {self.price}"


class Product(models.Model):
    STATUS_CHOICES = (
        ("pending", "PENDING"),
        ("delivered", "DELIVERED"),
        ("return", "RETURN")
    )

    Weight = models.ForeignKey(Weight, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    contact1 = models.CharField(max_length=255)
    contact2 = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    remarks = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name 

    def save(self, *args, **kwargs):
        if self.pk is None: 
            self.status = "pending"
        super().save(*args, **kwargs)






