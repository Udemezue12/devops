from uuid import uuid4
from django.contrib import admin
from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator
from django.core.files.images import ImageFile
from django.contrib.auth.models import User


from store.validators import validate_file_size


# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Product(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    last_update = models.DateTimeField(auto_now=True)
    # last_update = models.DateTimeField(auto_now=True)

    slug = models.SlugField()
    collection = models.ForeignKey(
        'Collection', on_delete=models.PROTECT, related_name='products')
    promotions = models.ManyToManyField(Promotion, blank=True)
    inventory = models.IntegerField(
        validators=[MinValueValidator(0)], default=0)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class ProductImage(models.Model):

    def default_image():
        with open('media/store/images', 'rb') as f:
          return ImageFile(f) 
    

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(
        upload_to='store/images',
        validators=[validate_file_size], default='default_image.jpg')


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    # phone = models.CharField(max_length=255)
    birth_date = models.DateField()
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    # user = models.OneToOneField(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Returns a string representation of the customer, consisting of their first name and last name."""
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        """Returns the customer's first name."""
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        """Returns the customer's last name."""
        return self.user.last_name


class Collection(models.Model):
    """
    Represents a collection of products.
    """

    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name='+', blank=True)

    def __str__(self) -> str:
        """
        Returns the title of the collection as a string.
        """
        return self.title

    class Meta:
        ordering = ['title']


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.CharField(max_length=255)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    class Meta:
        permissions = [
            ('cancel_order', 'Can cancel order'),
            ('send_order', 'Can send order')

        ]


class OrderItem(models.Model):
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='items')
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name='orderitems')


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
