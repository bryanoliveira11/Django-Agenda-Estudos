from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contacts,
        'site_title': "Contatos |"
        }

    return render(request, 'contact/index.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
            ) \
        .order_by('-id')

    context = {
        'contacts': contacts,
        'site_title': f"Search |"
        }

    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    single_contact = get_object_or_404(
        Contact.objects.filter(pk=contact_id, show=True))

    contact_name = f"{single_contact.first_name} {single_contact.last_name}"

    context = {
        'contact': single_contact,
        'site_title': f" {contact_name} |"
    }

    return render(request, 'contact/contact.html', context)