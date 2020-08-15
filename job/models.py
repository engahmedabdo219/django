from django.db import models

job_Type=(('full time','full time'),('part time','part time'),)
# Create your models here.
class job(models.Model):
    title = models.CharField(max_length=100)
    
    
    job_type = models.CharField(max_length=15 ,choices=job_Type)
    discription=models.TextField(max_length=1000)
    poblished_at=models.DateTimeField( auto_now=True)
    vacancy=models.IntegerField(default=1)
    Salary=models.IntegerField(default=1000)
    experience=models.IntegerField(default=1)


    def __str__(self):
        return self.title
    

