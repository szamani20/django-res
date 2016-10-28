import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Member


@csrf_exempt
def search(request):
    if request.method == 'GET':
        criteria = request.GET.get('q', '')

        if criteria != '':
            items = list(Member.objects.filter(
                name__icontains=criteria))
            if items:
                items = [x.get_profile().__dict__ for x in items]
                return HttpResponse(json.dumps(items), status=200,
                                    content_type="application/json")
            else:
                return HttpResponse(status=400, content_type='text/plain',
                                    content='No result')
