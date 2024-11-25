from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, default=0)
    age = models.IntegerField(default=0)
    course = models.CharField(max_length=100, default=0)
    place = models.CharField(max_length=150, default=0)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    f_name = models.CharField(max_length=50, default=0)
    l_name = models.CharField(max_length=50, default=0)
    username = models.CharField(max_length=50, default=0)
    email = models.EmailField()
  
class Items(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    desription = models.CharField(max_length=150)


# one-to-one relation
# one-many relation


#st = Student.objects.all() 
#st = Students.objects.filter(course="python")
#s = Student(name='value1', age='value2', course='value3')
#s.save()
#delete()