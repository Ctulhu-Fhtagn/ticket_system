from django.contrib import admin
from ticket_system.ticket.models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     pass
