from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    '''Class-based view for the homepage.'''
    template_name = "public/home.html"


class AboutPageView(TemplateView):
    template_name = "public/about.html"


class ContactPageView(TemplateView):
    template_name = "public/contact.html"


class LoginPageView(TemplateView):
    template_name = "public/login.html"


class LogoutView(TemplateView):
    '''TODO: This makes no sense, make this a view that redirects to login'''
    template_name = "public/logout.html"
