from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request,'food/index.html', context)

    # template = loader.get_template('food/index.html')
    # return HttpResponse(template.render(context, request))


def detail(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'item': item
    }
    return render(request, 'food/detail.html', context)
