from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'pages/home.html', context={}, status=200)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIWE
    Conume by JavaScript/Swift/Java/iOS/Android
    return json data
    """
    data = {
        "id": tweet_id
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404


    return JsonResponse(data, status=status)


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "response": tweets_list
    }
    return JsonResponse(data)