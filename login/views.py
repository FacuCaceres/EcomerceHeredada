from multiprocessing import context
from django.shortcuts import redirect, render

#Importamos un modelos de formulario para validar correos y demas utlilidades.
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #UserCreationForm Crea un registro con usuario del DB


# Importamos una funcion que verfica que el usuario y contraseña que vienen por POST son iguales a los de las DB.
from django.contrib.auth import authenticate,login,logout #LOGIN simplemente me logea



def login_user(request):
    # Si el metodo es POST
    if request.method == 'POST':
        # Creame una variable 'form' con los datos que viene por POST
        form = AuthenticationForm(request, data = request.POST)

        # Y si el formulario es valido.
        if form.is_valid():
            # Creame 2 variable de USERNAME Y PASSWORD con los datos limpios que vienen por POST
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # AUTHENTICATE me devuelve el usuario si existe en la BD sino me devuelve NONE
            user = authenticate(username=username, password=password)

            # Si el usuario es distinto de None es decir si me devuelve un usuario es porque hay uno en BD
            if user is not None:

                # Logeame ese USUARIO
                login(request,user)

                context = {'message':f'BIENVENIDO {username}!!! :D :D :D'}
                return render(request,'inicio/inicio.html',context=context)
            else: 
                context = {'error':'No existen usuarios con esas credenciales'}
                form = AuthenticationForm()
                return render (request,'login/login.html',context=context)
        else:
            # Y si no es no es valido Guardamos los errores en una variable de nombre errores
            errors = form.errors

            # Creamos nuevamente un objeto formulario con AuthenticationForm() 
            form = AuthenticationForm()

            # Pasamos este formulario limpio y los errores en un contexto
            context = {'error':errors,'forms':form}

            # Y por ultimo renderizamos todo en el LOGIN.html
            return render (request,'login/login.html',context=context)
        

    else:
        # Sino si el metodo es GET creame un formulario de AUTENTICACION
        form = AuthenticationForm()
        context = {'forms': form }

        # Luego renderizame ese formulario en un contexto al LOGIN.html
        return render (request,'login/login.html',context=context)


def logout_user(request):
    logout(request)
    return redirect('inicio')    

def register_user(request):
    # Si el metodo es POST 
    if request.method == 'POST':
        # Creame un modelo de form UserCreationForm con los datos de REQUEST.POST
        form = UserCreationForm(request.POST)
        # Y si es formulario es valido.
        if form.is_valid():
            # Guardame el formulario
            form.save()
            # Creame una username y pasword con datos limpios
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Autenticame este usuario
            user = authenticate(username = username , password = password)
            # Ahora logeame este usuario
            login(request,user)
            # Pasale el usario logeado en un contexto
            context = {'message': f'Usiario creado correctamente, bienvenido {username}'}
            # Por ultimo renderizame todo al inicio
            return render(request,'inicio/inicio.html',context=context)

        # Y si formulario no es valido...
        else:
            # Guardame los errores en una variable error
            error = form.errors
            # creame una nueva instancia de formulario
            form = UserCreationForm()
            # Pasame el nuevo formulario y el error por contexto
            context = {'forms':form, 'error': error}
            # Renderizame todo al register.html
            return render(request,'login/register.html',context=context)

    else:
        # Y si el metodo es GET "Crea un formulario de este modelo"
        form = UserCreationForm()
        # Carga en el contexto
        context = {'forms':form}
        # Y renderiza todo al register.html
        return render (request, 'login/register.html',context=context)
