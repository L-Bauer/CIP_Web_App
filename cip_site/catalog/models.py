from django.db import models

# Create your models here.

class Shift(models.Model):
    """Model representing a work shift."""
    name = models.CharField(max_length=15, help_text='Enter a work shift (e.g. 1st Shift)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class Dept(models.Model):
    """Model representing a work department"""
    name = models.CharField(max_length=20, help_text='Enter a work department')
    
    def __str__(self):
        return self.name
    
class Status(models.Model):
    """Model representing the working status"""
    name = models.CharField(max_length=20, help_text='Enter a status for the CIP (e.g. In-Process)')
    
    def __str__(self):
        return self.name
    
class CIP_Classification(models.Model):
    """Model representing the classification of the CIP"""
    name = models.CharField(max_length=100, help_text='Enter a classification for the CIP')
    
    def __str__(self):
        return self.name
    
class Asset(models.Model):
    """Model representing an Asset"""
    asset_num = models.CharField(max_length=20, help_text='Enter the asset number')
    
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
    
class CIP_Idea(models.Model):
    # Model representing the CIP entry
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular CIP entry')
    
    originator = models.ForeignKey('Associate', on_delete=models.PROTECT, null=True, 
                                   help_text="Enter associated that created the CIP Idea")
    
    entered_date = models.DateField.auto_now_add
    
    assets = models.ManyToManyField(Asset)
    
    status = models.OneToOneField(Status, on_delete=models.CASCADE)
    
    cip_class = models.ManyToManyField(CIP_Classification)
    
    start_date = models.DateField(null=True, blank=True)
    
    completed_date = models.DateField(null=True, blank=True)
    
    eng_support = models.ForeignKey('Associate', on_delete=models.PROTECT, null=True, 
                                    help_text="Enter associate supporting CIP")
    
    annual_savings = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.name
    