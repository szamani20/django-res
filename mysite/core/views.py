from django.shortcuts import render


def home(request):
    if request.user.is_authenticated():
        pass
    return render(request, 'core/home.html')
