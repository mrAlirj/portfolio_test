from django.shortcuts import render

def IndexPage(request):
    return render(request , 'index.html' )
