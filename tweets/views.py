from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")



def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIWE
    Conume by JavaScript/Swift/Java/iOS/Android
    return json data
    """
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404

    data = {
        "id": tweet_id,
        "content": obj.content,
        # "image_path": obj.image.url
    }
    # return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}</h1>")
    return JsonResponse(data)