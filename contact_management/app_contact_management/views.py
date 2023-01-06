from django.shortcuts import render, redirect
from .models import Contact


# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    # search_input = request.GET.get('search-area')
    # if search_input:
    # contacts = Contact.objects.filter(first_name_icontains=search_input)
    return render(request, 'index.html', {"contacts": contacts})


def addContact(request):
    if request.method == "POST":
        new_contact = Contact(
            first_name=request.POST["first_name"],
            second_name=request.POST["second_name"],
            patronymic=request.POST["patronymic"],
            organization=request.POST["organization"],
            position=request.POST["position"],
            email=request.POST["email"],
            phone_number=request.POST["phone_number"]
        )
        new_contact.save()
        return redirect("/")
    return render(request, "new.html")


def contactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, "contact-profile.html", {"contact": contact})


def editContact(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, "edit.html", {"contact": contact})
