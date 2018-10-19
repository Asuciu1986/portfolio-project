<<<<<<< HEAD
from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
=======
from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
>>>>>>> 7e1c5f01d4ee74ad5c84e9a1731b00dada0bc069
