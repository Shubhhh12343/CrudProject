from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    contact=models.CharField(max_length=200,null=True,blank=True)
    age=models.IntegerField(default=0)
    description=models.TextField(max_length=200)

    def ___str__(self):
        return self.email