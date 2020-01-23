from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_executor = models.BooleanField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    is_manager = models.BooleanField()

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Department(models.Model):
    name = models.TextField()
    description = models.TextField()


class Tag(models.Model):
    text = models.CharField(max_length=20)

    def __str__(self):
        return self.text

class Task(models.Model):
    client = models.ForeignKey(Client, related_name = 'client', null = True, on_delete=models.SET_NULL)
    executor = models.ForeignKey(Client, related_name = 'executor', null = True, on_delete=models.SET_NULL)
    title = models.TextField()
    text = models.TextField()
    PRIORITY_CHOICES = [
        ('n', 'normal'),
        ('l', 'low'),
        ('h', 'high'),
    ]
    priority_client = models.CharField(
        choices =  PRIORITY_CHOICES,
        max_length = 1,
        default = 'n',
        help_text = 'For chosing priority your task',
    )
    priority_executor = models.CharField(
        choices =  PRIORITY_CHOICES,
        max_length = 1,
        default = 'n',
    )
    STATUS_CHOICES = [
        ('2d','todo'),
        ('iw','inwork'),
        ('rv','review'),
        ('dn','done'),
        ('pp','postponed')
    ]
    status = models.CharField(
        choices = STATUS_CHOICES,
        max_length = 10,
        default = '2d'
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
