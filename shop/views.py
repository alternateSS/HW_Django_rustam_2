from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
from .models import Item
# Create your views here.


def greetings(request):
    return HttpResponse('Добро пожаловать в наш магазин!')


def list_item(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'list_item.html', context)

def detail_item(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        'item': item,
    }
    return render(request, 'detail_item.html', context)