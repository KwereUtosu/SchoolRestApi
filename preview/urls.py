from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('contact/add', views.ContactDetailView.as_view(), name='contact'),
    path('contact/list', views.ContactDetailView.as_view(), name='contact'),
    path('contact/view', views.ContactDetailView.as_view(), name='contact')
]