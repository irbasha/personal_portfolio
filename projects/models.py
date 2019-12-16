from django.db import models

class Project(models.Model):
	"""
	Project Model Class to store project information into the database
	Contains following fields and information

	Field name			- Description
	---------------------------------
	title				- CharField with the maximum length of data stored is limited to 100 characters
	description 		- TextField to store project's detailed information and limited to 1000 characters
	technology			- CharField with maximum length 100 characters
	image 				- FilePathField to store the relative path for the project's screenshot image
	"""
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)
	technology = models.CharField(max_length=100)
	image = models.FilePathField(path='images/')
