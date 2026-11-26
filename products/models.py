from django.db import models

# Create your models here.

class Product(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    product_name = models.CharField(max_length=200)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    product_image = models.ImageField(
        upload_to='products/'
    )

    seller_name = models.CharField(max_length=150)

    whatsapp_number = models.CharField(max_length=20)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    date_uploaded = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['-date_uploaded']