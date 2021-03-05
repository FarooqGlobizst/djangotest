from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="index"),
    path('farooq', views.farooq, name="farooq"),
    path("<str:name>", views.greet, name="greet")
]