from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Category
# Create your views here.


def index(request):
    ''' displays latest nine Categorys in closetclient/index.html '''
    latest_category_list = Category.objects.order_by('-pub_date')[:9]
    context = {
        'latest_category_list': latest_category_list,
    }
    return render(request, 'closetclient/index.html', context)


def detail(request, category_id):
    ''' displays single Category form in closetclient/details.html '''
    single_category = Category.objects.order_by('-category_name')
    context = {
        'single_category': single_category,
    }
    return render(request, 'closetclient/details.html', context)


def results(request, category_id):
    ''' displays Item results for a specific Category in closetclient/results.html '''
    response = "You're looking at the results of category %s."
    return HttpResponse(response % category_id)
# item count action
def item_count(request, category_id):
    ''' handles "item_count" for a particular "item_name" in a specific Category '''
    return HttpResponse("You're item_count on category %s." % category_id)
