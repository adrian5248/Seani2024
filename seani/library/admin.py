from django.contrib import admin

from .models import Module, Question

class ModuleAdmin(admin.ModelAdmin):
    name = 'module'
    verbose_name = 'Módulo'


# Register your models here.
    
admin.site.register(Module)
admin.site.register(Question)
