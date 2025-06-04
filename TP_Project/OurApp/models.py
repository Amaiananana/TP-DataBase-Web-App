from django.db import models

class UserProfile(models.Model):
    fname = models.CharField(max_length=100, verbose_name="First Name")
    mname = models.CharField(max_length=100, verbose_name="Middle Name", blank=True, null=True)
    lname = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(unique=True, primary_key=True, verbose_name="Email")
    password = models.CharField(max_length=100, verbose_name="Password")
    gender = models.CharField(max_length=100, choices=[
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Prefer not to say', 'Prefer not to say'),
    ], verbose_name="Gender")
    dob = models.DateField(verbose_name="Date of Birth")
    course = models.CharField(max_length=100, choices=[
        ('BSAIS', 'BS in Accounting and Information System'),
        ('BSCS', 'BS in Computer Science'),
        ('BSHM', 'BS in Hospitality Management'),
        ('BSIT', 'BS in Information Technology'),
        ('BSTM', 'BS in Tourism Management')
    ], verbose_name="Course")

    class Meta:
        db_table = 'UserProfile'


