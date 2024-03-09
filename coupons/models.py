from django.db import models
from django.core.validators import  MaxValueValidator, MinValueValidator
# Create your models here.

class Coupons(models.Model):
    code=models.CharField(max_length=15)
    valid_from=models.DateField()
    valid_to=models.DateTimeField()
    discount=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active=models.BooleanField()
    
    
    def __str__(self):
        return  self.code 
    