from django.db import models
import uuid

# Create your models here.
class MenProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description =models.TextField()
    date=models.DateField(auto_now=False, auto_now_add=True)
    time=models.TimeField(auto_now=False, auto_now_add=True)
    price=models.IntegerField()
    img = models.ImageField(upload_to='men',null=True,)
    def __str__(self):
        return self.title
    
