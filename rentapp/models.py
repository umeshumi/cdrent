from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	Name = models.CharField(max_length=25)
	Rent_Price = models.IntegerField()
	Image = models.ImageField(upload_to = 'ProductImage')
	Rented = models.BooleanField(default=False)
	Returned = models.BooleanField(default=False)

	def __str__(self):
		return self.Name


class Rent(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user 	= models.ForeignKey(User, on_delete=models.CASCADE)	
	days 	= models.IntegerField()
	actived = models.BooleanField(default=False)



	def  __str__(self):
		return self.product.Name

		
