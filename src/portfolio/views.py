from django.shortcuts import render
from .util import rss_parser, project_parser


def home_page(request):
    context = {'title': 'Home'}
    template_name = 'home.html'
    return render(request, template_name, context)


def resume_page(request):
    context = {'title': 'Resume'}
    template_name = 'resume.html'
    return render(request, template_name, context)


def about_page(request):
    context = {'title': 'About'}
    template_name = 'about.html'
    return render(request, template_name, context)


def projects_page(request):
    projects = project_parser.fetch_projects()
    context = {'title': 'Projects', 'projects': projects}
    template_name = 'projects.html'
    return render(request, template_name, context)


def blog_page(request):
    entries = rss_parser.get_feed()
    context = {'title': 'Blog', 'entries':entries}
    template_name = 'blog.html'
    return render(request, template_name, context)
