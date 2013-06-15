from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patron(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

class Address(models.Model):
	line_one = models.CharField(max_length=100)
	line_two = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zipcode = models.IntegerField()
	zipextension = models.IntegerField(null=True)

class PhoneNumber(models.Model):
	areacode = models.IntegerField()
	phone = models.IntegerField()

	def __unicode__(self):
		return '(' + str(self.areacode) + ')-' + str(self.phone)[:3] + '-' + str(self.phone)[3:]

class Shop(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=100)
	address = models.OneToOneField(Address)
	phone = models.OneToOneField(PhoneNumber)

	def __unicode__(self):
		return self.name

class Car(models.Model):
	owner = models.ForeignKey(Patron)
	make = models.CharField(max_length=50)
	model = models.CharField(max_length=50)
	color = models.CharField(max_length=50)
	year = models.IntegerField()

class Incident(models.Model):
	patron = models.ForeignKey(Patron)
	occurred = models.DateTimeField(auto_now_add=True)
	main_photo = models.OneToOneField('Photo', related_name='incident_main_photo')
	car = models.OneToOneField(Car)

class Photo(models.Model):
	image = models.ImageField(upload_to='incidents/%Y/%m/%d')
	incident = models.ForeignKey(Incident)

class ShopIncident(models.Model):
	shop = models.OneToOneField(Shop)
	incident = models.ForeignKey(Incident)
	is_favorite = models.BooleanField(default=False)

class Quote(models.Model):
	amount = models.DecimalField(max_digits=8, decimal_places=2)
	incident = models.ForeignKey(Incident)
	shop_incident = models.OneToOneField(ShopIncident)
	comments = models.TextField()