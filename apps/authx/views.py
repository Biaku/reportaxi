from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from apps.authx.forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Registro correctamente, ahora ya puedes publicar =)")
            return redirect('weblcient:publicar')
    else:
        form = SignUpForm()
    return render(request, 'authx/register.html', {'form': form})
