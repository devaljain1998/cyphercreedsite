from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse
# Create your models here.

class Profile(models.Model):
    BRANCH_CHOICES = [
        ('1','Computer Science Engineering'),
        ('2','Electronics and Communication Engineering'),
        ('3','Electrical engineering'),
        ('4','Mechanical Engineering'),
        ('5','Information Technology Engineering'),
        ('6','Civil Engineering'),
        ('7','Chemical Engineering'),
        ('8','Aeronautical Engineering'),
        ('9','Agricultural engineering'),
        ('10','Mining engineering'),
        ('11','Biochemical engineering'),
        ('12','Electrical and Instrumentation Engineering'),
        ('13','Metallurgical Engineering'),
    ]

    YEAR_CHOICES = (
        ('1','First Year'),
        ('2','Second Year'),
        ('3','Third Year'),
        ('4','Fourth Year'),
        ('5','Fifth Year'),
        ('6','Passout'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE,help_text="eg: johndoe101")
    college = models.CharField(max_length=100, blank=True,help_text="eg: Poornima College Of Engineering, Jaipur")
    year = models.CharField(choices=YEAR_CHOICES,help_text='Your current year',default=1,max_length=20)
    branch = models.CharField(max_length=50,choices=BRANCH_CHOICES,default=1,null=False,blank=False) 
    mobile = models.CharField(max_length=10,help_text="Enter your 10-digit Mobile Number",blank=True,null=True)
    cc_points = models.IntegerField(default=0)
    #technical_proficiencies
    #questions
    #answers
    #activity
    #avatar
    

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def get_absolute_url(self):
        return reverse('userprofile',{'pk':self.user.id})
    