from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Shift(models.Model):
    """Model representing a work shift."""
    name = models.CharField(max_length=15, help_text='Enter a work shift (e.g. 1st Shift)', unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class Dept(models.Model):
    """Model representing a work department"""
    name = models.CharField(max_length=20, help_text='Enter a work department', unique=True)
    
    def __str__(self):
        return self.name
    
class Status(models.Model):
    """Model representing the working status"""
    name = models.CharField(max_length=20, help_text='Enter a status for the CIP (e.g. In-Process)')
    
    def __str__(self):
        return self.name
    
class cipClassification(models.Model):
    """Model representing the classification of the CIP"""
    name = models.CharField(max_length=100, help_text='Enter a classification for the CIP')
    
    code = models.CharField(max_length=1, help_text='Enter the code for the classification (e.g. S for Safety)')
    
    def __str__(self):
        return self.name
    
class Asset(models.Model):
    """Model representing an Asset"""
    asset_num = models.CharField(max_length=20, help_text='Enter the asset number', unique=True)
    
    dept = models.ForeignKey('Dept', on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.name
    
class Associate(models.Model):
    """Model representing the associates"""
    emp_id = models.PositiveIntegerField(help_text='Enter the employees ID number')
    
    name = models.CharField(max_length=30, help_text="Enter in the associate's name")
    
    shift = models.ForeignKey('Shift', on_delete=models.PROTECT, null=True)
    
    dept = models.ForeignKey('Dept', on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.name
    
class cipIdea(models.Model):
    # Model representing the CIP entry
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular CIP entry')
    
    originator = models.ManyToManyField(Associate,related_name='originator', 
                                   help_text="Enter associated that created the CIP Idea")
    
    entered_date = models.DateField(auto_now_add=True)
    
    assets = models.ManyToManyField(Asset)
    
    status = models.OneToOneField(Status, on_delete=models.CASCADE)
    
    cip_class = models.ManyToManyField(cipClassification)
    
    start_date = models.DateField(null=True, blank=True)
    
    completed_date = models.DateField(null=True, blank=True)
    
    summary = models.CharField(max_length=1000, help_text="Enter the summary of the CIP idea")
    
    eng_support = models.ManyToManyField(Associate ,related_name='supporter', 
                                    help_text="Enter associate supporting CIP")
    
    annual_savings = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    def display_class(self):
        """Create a string for the classification. This is required to display genre in Admin."""
        return ', '.join(cip_class.name for cip_class in self.cip_class.all()[:3])

    display_class.short_description = 'CIP Class'

    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this CIP."""
        return reverse('cip-detail', args=[str(self.id)])