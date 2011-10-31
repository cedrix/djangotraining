from bugtracker.models import Project, Ticket
from django.contrib import admin
 
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
 
 
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title','project', 'tracker', 'priority', 'status', 'created_by', 'assign_to',)
    
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Ticket, TicketAdmin)
