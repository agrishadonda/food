from django.db import models


# Create your models here.
    
class banner(models.Model):
    img = models.ImageField(upload_to="images/")
    tital = models.CharField(max_length = 100)
    content = models.CharField(max_length = 200)
    para1 = models.CharField(max_length = 300)
    para2 = models.CharField(max_length = 300)
    
class TestModel(models.Model):
    email = models.EmailField()
    
class datemodel(models.Model):
    dates = models.DateField()
    
# class Dropdown(models.Model):
#     p = 'person'
#     p1 = 'person1'
#     p2 = 'person2'
#     p3 = 'person3'
    
#     person_choices = [
#         ('p', 'person1'),
#         ('p1','person2'),
#         ('p2','person3'),
#         ('p3','person4'),
#     ]
    
#     person_type = models.CharField('person',max_length = 10,choices=person_choices )


class StudentProfile(models.Model):
    fname = models.CharField(
        'Student First Name',
        max_length=50,
        
    )
    lname = models.CharField(
        'Student Last Name',
        max_length=50
    )
    date = models.DateField(
        'Student Date Of Birth'
    )

    # def __str__(self):
    #     return f'Student: {self.student_first_name} {self.student_last_name}'


class blog1(models.Model):
    image1 = models.ImageField(upload_to="images/")
    date = models.DateField()
    cont1 = models.CharField(max_length = 30)
    paragraph = models.CharField(max_length =300)
    

    