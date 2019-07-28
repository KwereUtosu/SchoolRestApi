from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.Contact_page.as_view(), name='contact')
]