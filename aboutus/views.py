from django.shortcuts import render

# Create your views here.
def aboutus(request):
    return render(request, 'aboutus/about.html',{'title':'About us'})

def contact(request):
    return render(request, 'aboutus/contactus.html',{'title':'Contact us'})