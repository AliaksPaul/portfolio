from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm
from django.template.loader import render_to_string

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('contactform.html', {
                'name': name, 
                'email': email,
                'message': message,
            })
             
            send_mail(name, 
                    message, 
                    email, 
                    ['paulouskaya.aliaksandra@gmail.com'], 
                    html_message=html)

            return redirect('/thanks/')
    else:
        form = ContactForm()

    
    home = Home.objects.latest('updated')
    about = About.objects.latest('updated')
    profile = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()

    context = {
        'home': home,
        'about': about,
        'profile': profile,
        'categories': categories,
        'portfolios': portfolios,
        'form': form, 
    }
    
    return render(request, 'index.html', context)


def thanks(request):
    return render(request, 'thanks.html')
