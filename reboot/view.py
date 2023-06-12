from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
        if request.method == "GET":
            template = loader.get_template("index.html")
