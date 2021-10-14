from django.db import models #importing prewritten django code about models
from django.conf import settings
from django.utils import timezone

# Create your models here.models are created the way we create a class in python. 
import datetime


from django.core.validators import MaxValueValidator, MinValueValidator
#import phonenumber


from django.db import models

# Create your models here.



def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)



GENDER=(
    ("MALE","MALE"),
    ("FEMALE","FEMALE"),
    ("NON-BINARY","NON-BINARY"),
    ("TRANSGENDER","TRANSGENDER"),

)

class Student(models.Model):#use the class keyword model.model just tells jango that Student is a django model that needs to be  saved in the DB
    #LIST THE PROPERTIES THAT YOU WANT YOUY STUDENT TO STORE IN THE dATAABASE AND SPECIFY THE DATA TYPE
    
    first_name = models.CharField(max_length=12) 
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    birth_date =models.DateField(default='yyyy-mm-dd')
    nationality=models.CharField(max_length=20) 
    gender = models.CharField(max_length=20, choices = GENDER,default='FEMALE')
    national_id = models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    admission_date =models.DateField()
    guardian_name = models.CharField(max_length=30)
    guardian_phone_number = models.CharField(max_length=20)
    medical_report=models.FileField(upload_to='documents/%Y/%m/%d')
    room_number = models.PositiveSmallIntegerField(null=True,blank=True)
    class_name =models.CharField(max_length=20,null=True,blank=True)
    academic_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984),max_value_current_year])
    email =models.EmailField()
    city =models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')

    
    def __str__(self):#defining how to I dentify this entity as a string.a model is saved into a db table. a db is created to correspond to one database model.

        return self.first_name

       



     