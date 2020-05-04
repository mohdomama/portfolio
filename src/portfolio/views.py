from django.shortcuts import render


def home_page(request):
    context = {'title': 'Home Page'}
    return render(request, "base.html", context)
