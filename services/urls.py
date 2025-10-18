from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.service_providers, name='service_providers'),
    path('providers/', views.provider_list, name='provider_list'),
    path('providers/<int:provider_id>/', views.provider_detail, name='provider_detail'),
    path('become-provider/', views.become_provider, name='become_provider'),
    path('provider-dashboard/', views.provider_dashboard, name='provider_dashboard'),
]
