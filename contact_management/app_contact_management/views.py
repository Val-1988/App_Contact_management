from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Contact
from django.db.models import CharField, Value
from django.db.models.functions import Concat


# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.annotate \
            (full_name=Concat('first_name', Value(' '), 'second_name', output_field=CharField())
             ).filter(Q(first_name=search_input, second_name=search_input, full_name=search_input, _connector=Q.OR))
    else:
        contacts = Contact.objects.all()
        search_input = ""
    return render(request, 'index.html', {"contacts": contacts, "search_input": search_input})


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

    if request.method == "POST":
        contact.first_name = request.POST["first_name"]
        contact.second_name = request.POST["second_name"]
        contact.patronymic = request.POST["patronymic"]
        contact.organization = request.POST["organization"]
        contact.position = request.POST["position"]
        contact.email = request.POST["email"]
        contact.phone_number = request.POST["phone_number"]
        contact.save()
        return redirect("/profile/" + str(contact.id))
    return render(request, "edit.html", {"contact": contact})


def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == "POST":
        contact.delete()
        return redirect("/")
    return render(request, "delete.html", {"contact": contact})
