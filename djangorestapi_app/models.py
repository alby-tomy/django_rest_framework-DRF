from django.db import models

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=20)
    
    def __str__(self)->str:
        return self.team_name

class Person(models.Model):
    team = models.ForeignKey(Team,default=None,null =True, blank=True, on_delete=models.CASCADE, related_name="team_members")
    name = models.CharField(max_length=50)
    email = models.EmailField(default='default@gmail.com')
    age = models.IntegerField(default=18)
    password = models.CharField(default='default@123',max_length=50)              