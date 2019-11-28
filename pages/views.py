from django.shortcuts import render
from properties.models import Propertie
from agents.models import Agent
from properties.choices import state_choices, price_choices, bedroom_choices
from django.contrib.auth.decorators import login_required
from contacts.models import Contact

def index(request):
    properties = Propertie.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    context = {
        'properties':properties,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
    }
    
    template_name = 'pages/index.html'
    
    return render(request, template_name, context)


def about(request):
    agents = Agent.objects.order_by('-hire_date')
    
    mvp_agents = Agent.objects.all().filter(is_mvp=True)
    
    context = {
        'agents':agents,
        'mvp_agents': mvp_agents
    }
    template_name = 'pages/about.html'
    
    return render(request, template_name, context)


def developments(request):
    template_name = 'pages/developments.html'
    return render(request, template_name)


def blog(request):
    template_name = 'pages/blog.html'
    return render(request, template_name)


def contact(request):
    template_name = 'pages/contact.html'
    return render(request, template_name)

@login_required
def dashboard(request):
    contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    
    context = {
        'contacts':contacts,
    }
    
    template_name = 'account/dashboard.html'
    return render(request, template_name, context)


