from django.shortcuts import render


# Create your views here.
def auth(request):
        return render(request, "BOAU.html")

def coauth(request):
        return render(request, "BOCO.html")

def ed(request):
        return render(request, "BOED.html")
