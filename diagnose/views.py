from django.shortcuts import render

# Create your views here.
def mainDiagnose(request):
    return render(request, 'diagnose/main.html',{'title':'Find disease'})
