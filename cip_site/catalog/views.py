from django.shortcuts import render
from django.db.models import Sum
from .models import cipClassification, cipIdea, Asset, Associate, Dept

# Create your views here.
def index(request):
    """View function for home page of site"""
    
    # Generate cost for some of the main objects
    num_cip = cipIdea.objects.all().count()
    total_saving = cipIdea.objects.aggregate(Sum('annual_savings'))
            
    context = {
        'num_cip': num_cip,
        'total_saving': total_saving.values(),
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)