from django.shortcuts import render

# Create your views here.
def weed(request):
    return render(request, 'weed/weed.html',{'title':'Weed Control'})

def weedcam(request):
    return render(request, 'weed/camera.html',{'title':'Weed Control - camera'})