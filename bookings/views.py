from django.shortcuts import render, redirect
from .models import Job

def post_job(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        budget = request.POST['budget']
        # Create job logic here
        return redirect('home')
    return render(request, 'post_job.html')
