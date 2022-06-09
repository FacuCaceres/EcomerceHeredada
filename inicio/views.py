from django.shortcuts import render

# Create your views here.
def inicio (request):
    print(request.user)
    print(request.user.is_authenticated)
    return render(request,'inicio/inicio.html')