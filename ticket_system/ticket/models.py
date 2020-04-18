from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_executor = models.BooleanField()
    department = models.ForeignKey('Department', blank=True, null=True, on_delete=models.SET_NULL)
    is_manager = models.BooleanField()

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return f'{self.pk}: {self.full_name}'

    def get_random(queryset):
        return queryset.order_by("?").first()

class Department(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.pk}: {self.name}'


class Task(models.Model):
    
    # class Meta:
    #     permissions = ( ("can_create_task", "User Can Create a new task"),
    #                     ("can_update_task", "User Can update a task"),
    #                     )

    PRIORITY_CHOICES = [
        ('n', 'Normal'),
        ('l', 'Low'),
        ('h', 'High'),
    ]
    PRIORITY_CHOICES_DICT = {
        x[0]: x[1] for x in PRIORITY_CHOICES
    }

    STATUS_CHOICES = [
        ('2d','To do'),
        ('iw','Inwork'),
        ('rv','Review'),
        ('dn','Done'),
        ('pp','Postponed')
    ]

    STATUS_CHOICES_DICT = {
        x[0]: x[1] for x in STATUS_CHOICES
    }
    
    client = models.ForeignKey(Client, related_name = 'client', null = True, on_delete=models.SET_NULL)
    executor = models.ForeignKey(Client, related_name = 'executor', null = True, on_delete=models.SET_NULL)
    title = models.TextField()
    text = models.TextField()

    priority = models.CharField(
        choices =  PRIORITY_CHOICES,
        max_length = 1,
        default = 'h',
        help_text = 'For chosing priority your task',
    )
        
    status = models.CharField(
        choices = STATUS_CHOICES,
        max_length = 10,
        default = '2d'
    )
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    tag = TaggableManager(blank=True)

    def __str__(self):
        return f'{self.pk}: {self.title}'

    
