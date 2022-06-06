from multiprocessing import context
from django.shortcuts import render
from . models import BioData
from django.db.models import Q
# Create your views here.

def index(request):
    # ? if there is [query] in request that we want to get 
    # * the [query] is from {input} element name inside the form.
    
    if 'query' in request.GET:
        
        # * this will get exacty the value you are passing into it.
        query_data = request.GET['query']
        # *  after querying the results we want to get the exact data we are lokking for.
        # biodatas = BioData.objects.filter(first_name__icontains=query_data)
        
        # * this can be to query multiple datas from the database
        multiple_queries = Q(Q(first_name__icontains=query_data) | Q(last_name__icontains=query_data) | Q(age__icontains=query_data) | Q(nationality__icontains=query_data))
        
        # * filtering the multiple queries
        biodatas = BioData.objects.filter(multiple_queries)
    else:
        biodatas = BioData.objects.all()
    context = {
        'biodatas' : biodatas
    }
    return render(request, 'searchapp/index.html', context)