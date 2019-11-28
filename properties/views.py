from django.shortcuts import render, get_object_or_404
from properties.models import Propertie
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import bedroom_choices, state_choices, price_choices
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def properties(request):
    properties = Propertie.objects.order_by('-list_date').filter(is_published=True)
    
    paginator = Paginator(properties, 2)
    
    page = request.GET.get('page')
    
    paged_listings = paginator.get_page(page)
    
    context = {
        'properties':paged_listings
        }
    template_name = 'pages/properties.html'
    return render(request, template_name, context)

@login_required
def _property(request, pk):
    
    property_o = get_object_or_404(Propertie, pk=pk)
    
    context = {'property_o':property_o}
    
    template_name = 'pages/property.html'
    
    return render(request, template_name, context)

@login_required
def search(request):
    query_list = Propertie.objects.order_by('-list_date')
    
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains=keywords)
    
    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)
    
    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)
            
    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__lte=bedrooms)
    
    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)
    
    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'properties': query_list,
        'values': request.GET,
    }
    template_name = 'pages/search.html'
    
    return render(request, template_name, context)
