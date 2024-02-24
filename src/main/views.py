from django.shortcuts import render, HttpResponse


def index(request):
    data = {}
    return render(request=request, template_name="index.html", context=data)