from django.shortcuts import render
from django.db.models import Sum
from django.views import generic
from .models import cipClassification, cipIdea, Asset, Associate, Dept, Status

# Create your views here.
def index(request):
    """View function for home page of site"""
    
    # Generate cost for some of the main objects
    num_cip = cipIdea.objects.all().count()
    total_saving = cipIdea.objects.aggregate(Sum('annual_savings'))
    
    num_in_process = cipIdea.objects.filter(status__name='In-Process').count()
            
    context = {
        'num_cip': num_cip,
        'total_saving': f"${total_saving['annual_savings__sum']}",
        'num_in_process': num_in_process,
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class CIPListView(generic.ListView):
    model = cipIdea
    
    context_object_name = 'cip_list'   # your own name for the list as a template variable
    