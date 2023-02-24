from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Dept(models.Model):
    """Model representing a work department"""
    name = models.CharField(max_length=20, help_text='Enter a work department', unique=True)
    
    def __str__(self):
        return self.name

class Status(models.Model):
    """Model representing a CIP Status"""
    name = models.CharField(max_length=20, help_text='Enter a status for CIP', 
                            unique=True, default="In-Process")
    
    def __str__(self):
        return self.name

    
class Asset(models.Model):
    """Model representing an Asset"""
    asset_num = models.CharField(max_length=20, help_text='Enter the asset number', unique=True)
    
    dept = models.ForeignKey('Dept', on_delete=models.PROTECT, null=True, blank=False)
    
    def __str__(self):
        return self.asset_num
    
class Associate(models.Model):
    """Model representing the associates"""
    emp_id = models.PositiveIntegerField(help_text='Enter the employees ID number', unique=True)
    
    name = models.CharField(max_length=30, help_text="Enter in the associate's name")
        
    dept = models.ForeignKey('Dept', on_delete=models.PROTECT, null=True)
    
    class Meta :
        ordering = ['name', 'dept']
    
    def __str__(self):
        return f' {self.name}, {self.dept.name}'
 
    
class cipIdea(models.Model):
    # Model representing the CIP entry
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular CIP entry')
    
    originator = models.ForeignKey(Associate, on_delete=models.PROTECT, related_name='originator')
    
    entered_date = models.DateField(auto_now_add=True)
    
    assets = models.ForeignKey(Asset, on_delete=models.PROTECT, help_text="Enter the asset related to the CIP Idea", null=True)

    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    
    summary = models.TextField( help_text="Enter the summary of the CIP idea")
    
    eng_support = models.ForeignKey(Associate, on_delete=models.PROTECT, related_name='supporter')
    
    annual_savings = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.originator.name} ({self.assets})'
    
    def is_in_process(self):
        return self.status == "In-Process"
        
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this CIP."""
        return reverse('cip-detail', args=[str(self.id)])