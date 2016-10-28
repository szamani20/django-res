from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserProfileForm, UserFoodForm


@login_required()
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        redirect_url = request.GET.get('next', reverse('core:home'))
        return HttpResponseRedirect(redirect_url)

    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'profile/profile.html',
                  context={'profile_form': form})


@login_required()
def add_food(request):
    if request.method == 'POST':
        form = UserFoodForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            added_food = form.instance
            added_food.restaurant_id = request.user.pk
            added_food.save()

            redirect_url = request.GET.get('next', reverse('core:home'))
            return HttpResponseRedirect(redirect_url)

    else:
        form = UserFoodForm()

    return render(request, 'profile/add_food.html',
                  context={'add_food_form': form})


@login_required()
def edit_food(request, pk=None):
    if not request.user.food_set:
        redirect_url = request.GET.get('next', reverse('core:home'))
        return HttpResponseRedirect(redirect_url)

    if request.method == 'POST':
        all_foods = list(request.user.food_set.all())
        for food in all_foods:
            if str(food.pk) == pk:
                form = UserFoodForm(data=request.POST, files=request.FILES, instance=food)
                if form.is_valid():
                    form.save()
                break

        redirect_url = request.GET.get('next', reverse('core:home'))
        return HttpResponseRedirect(redirect_url)

    all_foods = list(request.user.food_set.all())
    for food in all_foods:
        if str(food.pk) == pk:
            form = UserFoodForm(instance=food)
            return render(request, 'profile/edit_food.html',
                          {'form': form,
                           'food_to_edit': food})

    redirect_url = request.GET.get('next', reverse('core:home'))
    return HttpResponseRedirect(redirect_url)
