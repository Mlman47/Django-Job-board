from django.db import models

# Create your models here.

'''
Django Model field
    - HTML Widget 
    - Valdation
    - DB SIZE
'''
JOB_TYPE = [
        ("FT", 'Full Time'),
        ("PT", 'Part Time')
    ]
Gender=[
    ("M", 'Male'),
    ("F", 'Female'),
    ('A','Any')
]
class Job (models.Model):
    title=models.CharField(max_length=100) #Column
    # location
    job_type = models.CharField(max_length=20,choices=JOB_TYPE,default="")
    descriptions=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    # category
    experince=models.IntegerField(default=1)
    gender=models.CharField(max_length=10,choices=Gender)
    def __str__(self):
        return self.titlec