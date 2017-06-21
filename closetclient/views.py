from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.http import Http404


from .models import Category, Item
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
    return render(request, 'closetclient/detail.html', context)


def results(request, category_id):
    ''' displays Item results for a specific Category in closetclient/results.html '''
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'closetclient:results.html', {'category': category})


# item_count action
def item_count(request, category_id):
    ''' handles "item_count" for a particular "item_name" in a specific Category '''
    category = get_object_or_404(Category, pk=category_id)
    try:
        selected_item = category.item_set.get(pk=request.POST['item'])
    except (KeyError, Item.DoesNotExist):
        # redisplay the category item form
        return render(request, 'closetclient/detail.html', {
            'category': category,
            'error_message': "You have not selected an item.",
        })
    else:
        selected_item.item_count += 1
        selected_item.save()
        # return an HttpResponseRedirect after successfully dealing with POST data. prevents data from being posted twice if a user hits the back button.       
    return HttpResponseRedirect(reverse('closetclient:results', args=(category.id,)))










