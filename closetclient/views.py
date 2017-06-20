from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the closetclient index.")

def detail(request, category_id):
    return HttpResponse("You're looking at category %s." % category_id)

def results(request, category_id):
    response = "You're looking at the results of category %s."
    return HttpResponse(response % category_id)

def item_count(request, category_id):
    return HttpResponse("You're item_count on category %s." % category_id)

