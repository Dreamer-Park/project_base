from django.shortcuts import render

# Create your views here.

def landing(request):
    context={
                
    }
    return render(request, "landing/landing.html", context)