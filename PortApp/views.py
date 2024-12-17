from django.shortcuts import render, redirect
from . models import Profile, Skill, Contactmessage
from django.contrib import messages

# Create your views here.

def resume(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    return render(request, 'resume.html', {'profile': profile, 'skills': skills})

def contact(request):
      return render(request, 'contact.html')

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

    
        Contactmessage.objects.create(name=name, email=email, message=message)

        # Added success message to be shown in the template
        messages.success(request, "Thank you! Your message has been sent.")

        # Redirected to resume page after message submission
        return redirect('resume')

    return redirect('contact')  # Redirected back to the contact page if not POST