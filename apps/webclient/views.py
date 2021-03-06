from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import ListView

from apps.core.models import Taxi
from apps.webclient.forms import TaxiForm, TaxiBusquedaForm

from django.core.mail import send_mail, EmailMessage


def inicio(request):
    form = TaxiForm()
    variables = {'form': form}
    if request.method == 'POST':
        form = TaxiForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = request.user
            form.save()
            messages.success(request, "Publicacion guardada, gracias por colaborar =)")
            return redirect(reverse('webclient:inicio'))

    return render(request, 'webclient/index.html', variables)


class SeriviciosList(ListView):
    model = Taxi
    template_name = 'webclient/list.html'
    paginate_by = 10
    dato = None
    msg = None

    def get_queryset(self):
        numero = self.request.GET.get('number', None)
        if numero is not None:
            self.dato = numero
            taxis = Taxi.objects.filter(numero=numero)
            # form = TaxiBusquedaForm(self.request.GET)

            if taxis.count() != 0:
                return taxis
            else:
                self.msg = 'Aun no hay datos de este Taxi'
                return taxis
        return Taxi.objects.all().order_by('-created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dato'] = self.dato
        context['msj'] = self.msg
        return context


def busqueda(request):
    numero = request.GET.get('number', None)
    variables = {}
    if numero is not None:
        variables.update({'dato': numero})
        taxis = Taxi.objects.filter(numero=numero)

        if taxis.count() != 0:
            variables.update({'taxis': taxis})
        else:
            variables.update({'msj': 'Aun no hay datos de este Taxi'})
    else:
        raise Http404
    return render(request, 'webclient/busqueda.html', variables)


def publicar(request):
    form = TaxiForm()
    if request.method == 'POST':
        form = TaxiForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = request.user
            form.save()
            messages.success(request, "¡Publicado! gracias por colaborar =)")
            return redirect(reverse('webclient:servicios'))
    return render(request, 'webclient/publicar.html', {'form': form})


def tarifas(request):
    return render(request, 'webclient/tarifas.html')


def sectores(request):
    return render(request, 'webclient/sectores.html')


def sabias_que(request):
    return render(request, 'webclient/sabias_que.html')


def enviar_email(request):
    body = render_to_string('webclient/email_register.html', {'user': 'tavo', 'pass': 'asdasdasd'})
    email_message = EmailMessage(
        subject='Gracias por registrate.',
        body=body,
        from_email='REPORTAXI <email@reportaxi.com>',
        to=['tavo_x99@hotmail.com']
    )
    email_message.content_subtype = 'html'
    email_message.send()
    # send_mail('subject', 'body of the message', 'email@reportaxi.com',
    #           ['tavo_x99@hotmail.com', ])
    return HttpResponse("ok")


def error_404(request):
    data = {}
    return render(request, 'webclient/404.html', data)
