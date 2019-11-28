from django.contrib import admin
from .models import Agent

# Register your models here.
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job_description', 'email', 'hire_date', )
    list_display_links = ('id', 'name', )
    search_fields = ('name', )
    list_per_page = 25

admin.site.register(Agent, AgentAdmin)