from django.shortcuts import render
from .models import ServiceCategory, ServiceProvider

def home(request):
    categories = ServiceCategory.objects.all()
    return render(request, 'home.html', {'categories': categories})

def service_providers(request, category_id):
    providers = ServiceProvider.objects.filter(service_categories__id=category_id)
    return render(request, 'providers.html', {'providers': providers})
