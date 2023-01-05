from django.shortcuts import render, redirect
from .models import Contact


# Create your views here.

def index(request):
    return render(request, 'index.html')
    #contacts = Contact.objects.all()
    #search_input = request.GET.get('search-area')
    #if search_input:
        #contacts = Contact.objects.filter(first_name_icontains=search_input)


#def addContact(request):
    