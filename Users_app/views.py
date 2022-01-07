from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('Username')
            messages.success(request, f' Your account was created successfully, you can login now')
            return redirect('login')
            
    else:
        form = UserRegisterForm() 
    context = {
        'forms':form
    }
    return render(request, 'Users_app/register.html', context)
   
