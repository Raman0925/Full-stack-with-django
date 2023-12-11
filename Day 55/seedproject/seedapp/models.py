from django.db import models

# Create your models here.
class addList(models.Model):
    name = models.CharField(max_length = 30)
    first_name = models.CharField(max_length=255)
    roll = models.IntegerField()


class Student(models.Model):
    # Basic information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=10, unique=True)

    # Contact information
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Academic details
    date_of_birth = models.DateField()
    major = models.CharField(max_length=50, blank=True, null=True)
    graduation_year = models.PositiveIntegerField(blank=True, null=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
