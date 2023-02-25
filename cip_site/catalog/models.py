from django.db import models
from django.urls import reverse

# Create your models here.

class Dept(models.Model):
    """Model representing a work department"""
    name = models.CharField(max_length=20, help_text='Enter a work department', unique=True)
    
    def __str__(self):
        return self.name

class Status(models.Model):
    """Model representing a CIP Status"""
    WORK_STATUS = (
        ('i', 'In-Process'),
        ('c', 'Completed'),
        ('d', 'Deferred'),
    )

    status = models.CharField(
        max_length=1,
        choices=WORK_STATUS,
        blank=False,
        default='i',
        help_text='Enter a status for CIP',
    )
    
    def __str__(self):
        return self.status

    
class Asset(models.Model):
    """Model representing an Asset"""
    asset_num = models.CharField(max_length=20, help_text='Enter the asset number', unique=True)
    
    dept = models.ForeignKey('Dept', on_delete=models.PROTECT, null=True, blank=False)
    
    def __str__(self):
        return self.asset_num
    
class Associate(models.Model):
    """Model representing the associates"""
    emp_id = models.PositiveIntegerField(help_text='Enter the employees ID number', unique=True)
    
    first_name = models.CharField(max_length=30, help_text="Enter in the associate's first name")
    
    last_name = models.CharField(max_length=30, help_text="Enter in the associate's last name",
                                 blank=True, null=True)
        
    dept = models.ForeignKey('Dept', on_delete=models.PROTECT, null=True)
    
    
    def __str__(self):
        return f' {self.first_name}, {self.dept.name}, {self.emp_id}'
 
    
class cipIdea(models.Model):
    # Model representing the CIP entry
    originator = models.ForeignKey(Associate, on_delete=models.PROTECT, related_name='originator')
    
    entered_date = models.DateField(auto_now_add=True)
    
    assets = models.ForeignKey(Asset, on_delete=models.PROTECT, help_text="Enter the asset related to the CIP Idea", null=True)

    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    
    completed_date = models.DateField(blank=True, null=True)
    
    summary = models.TextField( help_text="Enter the summary of the CIP idea")
    
    eng_support = models.ForeignKey(Associate, on_delete=models.PROTECT, related_name='supporter')
    
    annual_savings = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.originator.first_name} ({self.id})'
    
    def is_in_process(self):
        return self.status == "In-Process"
        
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this CIP."""
        return reverse('cip-detail', args=[str(self.id)])