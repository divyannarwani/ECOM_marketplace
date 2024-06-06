from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from item.models import *

from .forms import SignupForm

# Create your views here.

def home(request):

    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    context = {'items':items, 'categories':categories}

    return render(request, 'core/home.html', context=context)



def contact(request):
    return render(request, 'core/contact.html')


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        
    else : 
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form':form
    })

@login_required
def logout_page(request):

    logout(request)
    return redirect("/login/")