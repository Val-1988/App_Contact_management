from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_contact/', views.addContact, name='add_contact'),
    path('profile/<str:pk>', views.contactProfile, name="profile"),
    path('edit_contact/<str:pk>', views.editContact, name='edit_contact')

]
