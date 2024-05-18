from django.db import models

# Create your models here.

# create company model
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                                                  ('Non IT','Non IT')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    company_image=models.FileField(upload_to="company/",max_length=300,null=True,default=None)
    def __str__(self):
      return self.name
  
#create employee models
class Employee(models.Model):
    # the on_delete=models.CASCADE automatically deletes all the employee of company if that company is deleted.
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(("Manager","Manager"),
                                                     ("Software Developer","Software Developer"),
                                                     ("Project Leader","Project Leader")))
    def __str__(self):
       return self.name