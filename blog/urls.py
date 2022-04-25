from django.urls import path
from . import views

urlpatterns = [
    path('hello',views.post_list, name='post_list'),
]
