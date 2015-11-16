from django.shortcuts import render
from .models import Contact

# Create your views here.

def index(request):
    return render(request, 'index.html')

def add_contact(request):
    if request.method == "POST":
        data = request.POST
        contact_data = {'first_name': data['first_name'],
                'last_name': data['last_name'],
                'main_number': data['main_number'],
                'email': data['email']}
        contact = Contact.objects.create(**contact_data)
        return render(request, 'success.html')
    return render(request, 'add_contact.html')

def view_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'view_contacts.html', context={'contacts': contacts})
