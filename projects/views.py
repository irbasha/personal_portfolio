from django.shortcuts import render
from .models import Project

def project_index(request):
	"""
	index view to list all the projects available with a link reference to each project and it displays below information for each project listed

	Title - title of the project
	Technology - technologies used to build this project
	Description - a small amount of description with a link to project's detail page
	"""
	projects = Project.objects.all()
	return render(request, 'project_index.html', {'projects': projects})

def project_detail(request, pin):
	"""
	project detail view showcasing all the necessary information regarding the particular project with below titles

	Image - A screenshot image of the project
	Title - Title of the Project
	About project - Description/Information about the project of what it is and what it does
	Technology - List of tools and technologies used in the project
	"""
	project = Project.objects.get(id=pin)
	return render(request, 'project_detail.html', {'project': project})
