import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Member, Food


def home(request):
    if request.user.is_authenticated():
        foods = list(request.user.food_set.all())

        return render(request, 'core/home.html', {'foods': foods})

    return render(request, 'core/home.html')


def fetch_shop_items(request, pk=None):
    foods = list(Food.objects.filter(restaurant_id=pk))
    if foods:
        foods = [x.get_food().__dict__ for x in foods]
        return HttpResponse(json.dumps(foods), content_type="application/json")
    else:
        return HttpResponse('Sishti')


def fetch_shop_profile(request, pk=None):
    shop = Member.objects.filter(id=pk)
    if shop:
        shop = shop[0]
        return HttpResponse(json.dumps(shop.get_profile().__dict__), content_type="application/json")
    else:
        return HttpResponse('Sishti')
