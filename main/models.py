from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#to make a class a model you only need to inherit from models.Model
#ORMs, a model describes the structure of table in a relational database


class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,default='task',blank=True,null=True)
    description = models.TextField(null=True,default='desc')
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']


    

