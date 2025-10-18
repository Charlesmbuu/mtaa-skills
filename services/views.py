from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ServiceProvider, ServiceCategory
from .forms import ServiceProviderForm

def home(request):
    """Home page with service categories"""
    categories = ServiceCategory.objects.all()
    return render(request, 'home.html', {'categories': categories})

def service_providers(request, category_id):
    """Show providers for a specific category"""
    providers = ServiceProvider.objects.filter(service_categories__id=category_id)
    category = get_object_or_404(ServiceCategory, id=category_id)
    return render(request, 'services/service_providers.html', {
        'providers': providers,
        'category': category
    })

def provider_list(request):
    """Show all service providers"""
    providers = ServiceProvider.objects.all()
    return render(request, 'services/provider_list.html', {'providers': providers})

def provider_detail(request, provider_id):
    """Show individual provider profile"""
    provider = get_object_or_404(ServiceProvider, id=provider_id)
    return render(request, 'services/provider_detail.html', {'provider': provider})

@login_required
def become_provider(request):
    """Allow users to become service providers"""
    if request.user.user_type != 'provider':
        messages.error(request, 'You must register as a provider first.')
        return redirect('register')
    
    # Check if user already has a provider profile
    try:
        provider = ServiceProvider.objects.get(user=request.user)
        messages.info(request, 'You already have a provider profile.')
        return redirect('provider_dashboard')
    except ServiceProvider.DoesNotExist:
        pass
    
    if request.method == 'POST':
        form = ServiceProviderForm(request.POST, request.FILES)
        if form.is_valid():
            provider = form.save(commit=False)
            provider.user = request.user
            provider.save()
            form.save_m2m()  # Save many-to-many data
            messages.success(request, 'Provider profile created successfully!')
            return redirect('provider_dashboard')
    else:
        form = ServiceProviderForm()
    
    return render(request, 'services/become_provider.html', {'form': form})

@login_required
def provider_dashboard(request):
    """Provider's personal dashboard"""
    try:
        provider = ServiceProvider.objects.get(user=request.user)
        return render(request, 'services/provider_dashboard.html', {'provider': provider})
    except ServiceProvider.DoesNotExist:
        messages.info(request, 'Please create your provider profile first.')
        return redirect('become_provider')
