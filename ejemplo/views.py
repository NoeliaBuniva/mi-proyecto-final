from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html",
    {
        "nombre":"noe",
        "apellido": "buniva",
    })

def index_tres(request):
    return render(request, "ejemplo/saludar.html", 
    {"notas":[1,2,3,4,5,6,7,8]}
    )