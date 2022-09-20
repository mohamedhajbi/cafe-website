from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.menu, name='menu'),
    path('list/<int:id>', views.list, name="list"),
]