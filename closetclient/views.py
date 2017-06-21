from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


from .models import Category, Item
# Create your views here.


class IndexView(generic.ListView):
    ''' displays latest nine Categorys in closetclient/index.html '''
    template_name = 'closetclient/index.html'
    context_object_name = 'latest_category_list'

    def get_queryset(self):
        """Return the last five published Categorys."""
        return Category.objects.order_by('-pub_date')[:9]


class DetailView(generic.DetailView):
    ''' displays single Category form in closetclient/details.html '''
    model = Category
    template_name = 'closetclient/detail.html'


class ResultsView(generic.DetailView):
    model = Category
    template_name = 'closetclient/results.html'


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










