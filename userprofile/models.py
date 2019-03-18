from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse
# Create your models here.

class Profile(models.Model):
    BRANCH_CHOICES = [
        ('Computer Science Engineering','Computer Science Engineering'),
        ('Electronics and Communication Engineering','Electronics and Communication Engineering'),
        ('Electrical engineering','Electrical engineering'),
        ('Mechanical Engineering','Mechanical Engineering'),
        ('Information Technology Engineering','Information Technology Engineering'),
        ('Civil Engineering','Civil Engineering'),
        ('Chemical Engineering','Chemical Engineering'),
        ('Aeronautical Engineering','Aeronautical Engineering'),
        ('Agricultural engineering','Agricultural engineering'),
        ('Mining engineering','Mining engineering'),
        ('Biochemical engineering','Biochemical engineering'),
        ('Electrical and Instrumentation Engineering','Electrical and Instrumentation Engineering'),
        ('Metallurgical Engineering','Metallurgical Engineering'),
    ]

    YEAR_CHOICES = (
        ('First Year','First Year'),
        ('Second Year','Second Year'),
        ('Third Year','Third Year'),
        ('Fourth Year','Fourth Year'),
        ('Fifth Year','Fifth Year'),
        ('Passout','Passout'),
    )

    AVATAR_CHOICES = (
        (1,'Beginner'),
        (2,'Bronze'),
        (3,'Silver'),
        (4,'Gold'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE, help_text="eg: johndoe101", related_name='profile')
    college = models.CharField(max_length=100, blank=True,help_text="eg: Poornima College Of Engineering, Jaipur")
    year = models.CharField(choices=YEAR_CHOICES,help_text='Your current year',default=1,max_length=20)
    branch = models.CharField(max_length=50,choices=BRANCH_CHOICES,default=1,null=False,blank=False) 
    mobile = models.CharField(max_length=10,help_text="Enter your 10-digit Mobile Number",blank=True,null=True)
    cc_points = models.IntegerField(default=0)
    #technical_proficiencies
    description = models.TextField(blank=True, help_text="Describe yourself, helps to connect with like-minded people.")
    #questions
    #answers
    #activity
    #avatar
    rating = models.PositiveIntegerField(default=1, choices=AVATAR_CHOICES)
    #urls
    github_url = models.URLField(blank=True, help_text="Showcase your projects through this. \n Your link to Github profile. eg: https://www.github.com/devaljain1998")
    linkedin_url = models.URLField(blank=True, help_text="Showcase your professional profile through this. \n Your link to LinkedIn profile. eg: https://www.linkedin.com/in/deval-sethi-00a2912a/")

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def get_absolute_url(self):
        return reverse('user_profile', {'pk':self.user.id})
    