from django.shortcuts import render

# Create your views here.
def pest(request):
    return render(request, 'pest/pest.html',{'title':'Pest Control'})

def pestcam(request):
    return render(request, 'pest/camera.html',{'title':'Pest Control - camera'})