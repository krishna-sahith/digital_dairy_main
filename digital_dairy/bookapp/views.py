from django.shortcuts import render


# Create your views here.
def auth(request):
        return render(request, "Book in/BOAU.html")

def coauth(request):
        return render(request, "Book in/BOCO.html")

def ed(request):
        return render(request, "Book in/BOED.html")
