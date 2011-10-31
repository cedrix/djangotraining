from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title
        
        
class Ticket(models.Model):
    TRACKER = (
        (1, u'RFC'),
        (3, u'Bug'),
        (5, u'Action'),
    )
    PRIORITY = (
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low') ,
    )
    STATUS  = (
        (1, 'New'),
        (2, 'In progress'),
        (3, 'Closed') ,
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project)
    tracker = models.IntegerField(max_length=1, choices=TRACKER)
    priority = models.IntegerField(max_length=1, choices=PRIORITY)
    status = models.IntegerField(max_length=1, choices=STATUS)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='creator')
    assign_to  = models.ForeignKey(User, blank=True, null=True, related_name='responsible')
