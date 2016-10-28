from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import OnlineOrder, OfflineOrder


@login_required()
def online_order(request, index=None):
    # TODO add an if where post request must handle different from get
    # index for now does that

    orders = list(OnlineOrder.objects.filter(restaurant_id=request.user.pk))

    if index:
        order_to_checkout = orders[int(index)]
        off_order = OfflineOrder(restaurant_id=request.user.pk,
                                 foods=order_to_checkout.foods,
                                 order_date=order_to_checkout.order_date,
                                 order_time=order_to_checkout.order_time,
                                 estimated_time=order_to_checkout.estimated_time,
                                 pending_time=20,
                                 customer=order_to_checkout.customer,
                                 rating=4.2)
        off_order.save()
        order_to_checkout.delete()

        redirect_url = request.GET.get('next', reverse('core:online_order'))
        return HttpResponseRedirect(redirect_url)

    foods = []
    for order in orders:
        food_order = ''
        price = 0
        for food in order.foods:
            food_order += food['title'] + ', ' + str(food['amount']) + \
                          ' times, each for ' + str(food['price']) + ' '
            price += food['price'] * food['amount']
        foods.append(food_order)

    # Maybe send the foods separately so less difficulty in template
    return render(request, 'order/online_order.html',
                  context={'order_list': zip(orders, foods)})


@csrf_exempt
def order_food(request):
    # TODO add an if where post request must handle

    response = HttpResponse(content='20', content_type='text/plain')
    data = json.loads(str(request.body, encoding='utf-8'))

    total_price = 0
    for food in data['foods']:
        total_price += food['price'] * food['amount']

    order = OnlineOrder(restaurant_id=data['shop_id'],
                        foods=data['foods'],
                        total_price=total_price,
                        estimated_time=20,
                        customer=data['customer'],
                        handled=False)

    # save order somewhere so the operator could handle it
    order.save()
    # then retrieve it for every member by filtering shop_id

    return response


@login_required()
def offline_order(request):
    pass
