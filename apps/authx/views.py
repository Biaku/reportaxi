from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

# Create your views here.
from apps.authx.forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Registrado correctamente, ahora ya puedes publicar =)")

            # enviando correo
            body = render_to_string('webclient/email_register.html', {'user': username, 'pass': raw_password})
            email_message = EmailMessage(
                subject='Gracias por registrate.',
                body=body,
                from_email='REPORTAXI <email@reportaxi.com>',
                to=[email]
            )
            email_message.content_subtype = 'html'
            email_message.send()
            return redirect('weblcient:publicar')
    else:
        form = SignUpForm()
    return render(request, 'authx/register.html', {'form': form})
