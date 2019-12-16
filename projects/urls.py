from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'), # project index view - shows list of projects
    path('<int:pin>/', views.project_detail, name='project_detail'), # project detail view - shows complete details of a project. View function takes an integer parameter conatining project id
]
