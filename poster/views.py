from typing import List
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class HomePageView(ListView):
    pass

class IndexView(ListView):
    pass

class DetailView(View):
    pass

class ReadLaterView(View):
    pass