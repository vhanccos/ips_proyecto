from django.db import models

# Create your models here.

#class Doctor(models.Model):
#    name = models.CharField(max_length=50)
#    mobile = models.IntegerField()
#    special = models.CharField(max_length=50)

#    def __str__(self):
#       return self.name;

from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
       return self.name
    
#######
class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=50)

    
    def __str__(self):
       return self.name;
#class Patient(models.Model):
 #   name = models.CharField(max_length=50)
  #  gender = models.CharField(max_length=10)
   # mobile = models.IntegerField(null=True)
    #address = models.CharField(max_length=50)
    #image1 = models.ImageField(upload_to='patient_images/', null=True, blank=True)
    #image2 = models.ImageField(upload_to='patient_images/', null=True, blank=True)
    #notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
       return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()


    def __str__(self):
       return self.doctorname+"--"+self.patient.name;

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.id
    
class Tooth(models.Model):
    TOOTH_CHOICES = [
        (f'T{i}', f'Tooth {i}') for i in range(1, 33)  # Asumiendo 32 dientes
    ]
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    tooth_number = models.CharField(max_length=3, choices=TOOTH_CHOICES)
    is_problematic = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.patient.name} - {self.get_tooth_number_display()}'
