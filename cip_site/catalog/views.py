from django.shortcuts import render
from django.db.models import Sum
from .models import cipClassification, cipIdea, Asset, Associate, Shift, Dept

# Create your views here.
def index(request):
    """View function for home page of site"""
    
    # Generate cost for some of the main objects
    num_cip = cipIdea.objects.all().count()
    total_saving = cipIdea.objects.aaggregate(Sum('annual_savings'))
    
    # In-Process CIPs
    num_instances_in_process = cipIdea.objects.filter(status__exact='I')
    
    context = {
        'num_cip': num_cip,
        'total_saving': total_saving,
        'num_instances_in_process': num_instances_in_process,
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)