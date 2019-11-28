from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        property_id = request.POST['property_id']
        properties = request.POST['properties']
        phone = request.POST['phone']
        email = request.POST['email']
        name = request.POST['name']
        message = request.POST['message']
        user_id = request.POST['user_id']
        agent_email = request.POST['agent_email']
        
        #check if user has made inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(property_id=property_id, user_id=user_id)
            
            if has_contacted:
                messages.error(request, 'You have made an inquiry about this listing')
                return redirect('/properties/'+ property_id)
        
        contact = Contact(property_id= property_id, properties = properties, phone= phone, email= email, name = name,
        message = message, user_id = user_id)

        contact.save()
        
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + properties + '. Sign into the admin for more information',
            'opraise139@gmail.com',
            [agent_email, 'opraise139@gmail.com'],
            fail_silently = False,
        )
        
        messages.success(request, 'Your request has been submitted, an Agent will get back to you soon')
        
        return redirect('/properties/'+ property_id)