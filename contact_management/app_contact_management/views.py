from django.shortcuts import render, redirect
from .models import Contact


# Create your views here.

def index(request):
    return render(request, 'index.html')
    # contacts = Contact.objects.all()
    # search_input = request.GET.get('search-area')
    # if search_input:
    # contacts = Contact.objects.filter(first_name_icontains=search_input)


def addContact(request):
    if request.method == "POST":
        new_contact = Contact(
            first_name=request.POST["first_name"],
            second_name=request.POST["second_name"],
            patronymic=request.POST["patronymic"],
            organization=request.POST["organization"],
            position=request.POST["position"],
            email=request.POST['email'],
            phone_number=request.POST['phone_number']
        )
        new_contact.save()
        return redirect("/")
    return render(request, 'new.html')
