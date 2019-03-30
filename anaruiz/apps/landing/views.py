from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .forms import ContactForm


def index(request):
    template = loader.get_template('landing/index.html')

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            subject = form.cleaned_data['asunto']
            from_email = form.cleaned_data['from_email']
            mensaje = 'Mensaje de: ' + nombre + '\nEmail: ' + from_email + '\n\n' + form.cleaned_data['mensaje']
            try:
                send_mail(subject, mensaje, 'info@anaruizromero.es', ['juan@quitiweb.com', 'anamail12@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            form = ContactForm()
            return redirect('mensaje-enviado')
        else:
            print('Error en el formulario')

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def mensaje_enviado(request):
    return render(request, 'landing/mensaje-enviado.html')


def cookies(request):
    return render(request, 'landing/cookies.html')
