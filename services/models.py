from django.db import models
from users.models import User

class ServiceCategory(models.Model):  # ← THIS MUST EXIST
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Service Categories"
    
    def __str__(self):
        return self.name

class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200)
    service_categories = models.ManyToManyField('ServiceCategory')
    description = models.TextField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # ADD THESE NEW FIELDS:
    experience_years = models.IntegerField(default=0)
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    profile_picture = models.ImageField(upload_to='provider_pics/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    
    # Provider metrics (we'll update these later)
    total_jobs_completed = models.IntegerField(default=0)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.business_name
    
    def get_absolute_url(self):
        return f"/providers/{self.id}/"
