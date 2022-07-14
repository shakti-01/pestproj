from django.shortcuts import redirect, render

from . forms import UserAddForm
from django.contrib import messages

# Create your views here.
def showSignup(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratulation! Account has been created successfully for {username}, now login again to verify')
            return redirect('login') #name = 'register' in urls.py
    else:
        form  = UserAddForm()
    return render(request, 'login/signup.html', {'form':form})