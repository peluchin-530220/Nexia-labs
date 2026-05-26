from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')




def contacto(request):

    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')

        contenido = f"""
        Nuevo mensaje desde NEXIA Labs

        Nombre: {nombre}
        Correo: {correo}

        Mensaje:
        {mensaje}
        """

        send_mail(
            subject='Nuevo mensaje desde la web',
            message=contenido,
            from_email='nexia.labs1@gmail.com',
            recipient_list=['nexia.labs1@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Mensaje enviado correctamente')

    return render(request, 'contacto.html')

def sobre(request):
    return render(request, 'sobre.html')