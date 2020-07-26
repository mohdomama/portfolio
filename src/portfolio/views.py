from django.shortcuts import render


def home_page(request):
    context = {'title': 'Home Page'}
    template_name = 'home.html'
    return render(request, template_name , context)
