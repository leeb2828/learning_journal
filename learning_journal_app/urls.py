from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<title>/<date>', views.detail, name='detail'),
    path('edit/<title>/<date>', views.edit, name='edit'),
    path('new/', views.new, name='new'),
    path('delete/<title>/<date>', views.delete, name='delete'),
]