<<<<<<< HEAD
from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request,'jobs/home.html', {'jobs':jobs})
=======
from django.shortcuts import render

from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
>>>>>>> 7e1c5f01d4ee74ad5c84e9a1731b00dada0bc069
