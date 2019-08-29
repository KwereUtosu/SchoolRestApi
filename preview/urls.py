from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('contact/add', views.ContactCreatView.as_view(), name='contact'),
    path('contact/update', views.ContactCreatView.as_view(), name='contact'),
    path('contact/list', views.ContactListView.as_view(), name='contact-list'),
    path('contact/<int:pk>', views.ContactDetailView.as_view(), name='contact-detail'),
    path('person/add', views.PersonnelCreatView.as_view(), name='person'),
    path('person/list', views.PersonnelListView.as_view(), name='person-list'),
    path('person/<int:pk>', views.PersonnelDetailView.as_view(), name='person-detail')

]