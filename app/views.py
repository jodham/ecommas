from django.shortcuts import render
# Create your views here.
def myapp(request):
    return render(request, 'index.html'),
