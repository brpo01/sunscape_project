from django.shortcuts import render, redirect
from properties.models import Propertie
from agents.models import Agent
from properties.choices import state_choices, price_choices, bedroom_choices
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
from django.contrib import messages

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
    if request.method == 'POST':
        message = request.POST['message']
        
        #check if user has made inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id)
            
            if has_contacted:
                messages.error(request, 'You have made contact already')
                return redirect('contact')
            
        contact = Contact(message=message)
        contact.save()
        
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + properties + '. Sign into the admin for more information',
            'opraise139@gmail.com',
            [agent_email, 'opraise139@gmail.com'],
            fail_silently = False,
        )
        
        messages.success(request, 'Your request has been submitted')
        
        return redirect('index')
        
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


