from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now_add=True)
	categories = models.ManyToManyField('Category', related_name='posts')

	def __str__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Comment(models.Model):
	author = models.CharField(max_length=20)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)