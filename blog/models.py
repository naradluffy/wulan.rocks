import datetime

from django.db import models
from django.utils import timezone


class Project(models.Model):
	title = models.CharField(max_length=300)
	little_description = models.CharField(max_length=300,null=True)
	description = models.TextField()
	featured_image = models.CharField(max_length=300)
	source_image = models.CharField(max_length=100,null=True)
	source_image_link = models.URLField(null=True)
	url_link = models.URLField(null=True)
	rating = models.IntegerField(default=0)
	pub_date = models.DateTimeField(default=timezone.now)
	categories = models.ManyToManyField('Category')
	trinket = models.TextField(null=True)
	def __str__(self):
		return self.title
		

class Comment(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
	email = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	message = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.name
	

class Category(models.Model):
	cat_name = models.CharField(max_length=100)
	image = models.CharField(max_length=20,null=True)
	description = models.CharField(max_length=350,null=True)
	
	def __str__(self):
		return self.cat_name

class Contact(models.Model):
	subject = models.CharField(max_length=200)
	email = models.CharField(max_length=100)
	message = models.TextField()
	send_date = models.DateTimeField(default=timezone.now)

class Picture(models.Model):
	slug = models.CharField(max_length=50)
	alt = models.CharField(max_length=200)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
	url_link = models.URLField()
	source_image = models.CharField(max_length=100,null=True)
	source_image_link = models.URLField(null=True)
	
	def __str__(self):
		return self.url_link