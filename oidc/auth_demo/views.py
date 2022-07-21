from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    # template = loader.get_template('auth_demo/index.html')
    # return HttpResponse(template.render(request))
    context = {}
    return render(request, 'auth_demo/index.html', context)
