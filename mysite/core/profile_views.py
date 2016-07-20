from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserProfileForm


@login_required()
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'profile/profile.html',
                  context={'profile_form': form})


def user_profile(request):
    return 'Not implemented yet :('
