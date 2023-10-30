from profile import Profile
from django.db import models
from django.contrib.auth.models import User
import uuid
from tinymce import models as tinymce_models

# Create your models here.
class Catagories(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    catagory=models.ForeignKey(Catagories, on_delete=models.DO_NOTHING)
    description =tinymce_models.HTMLField()
    date=models.DateField(auto_now=False, auto_now_add=True)
    time=models.TimeField(auto_now=False, auto_now_add=True)
    price=models.IntegerField()
    img = models.ImageField(upload_to='men',null=True,)
    def __str__(self):
        return self.name
    
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    def __str__(self):
        return f"Cart for {self.user.username}"
    
User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
User.cart = property(lambda u: Cart.objects.get_or_create(user=u)[0])

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} X {self.product.name}"