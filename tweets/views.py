import random
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import TweetForm
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
    tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 200)} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    # print("post data is: ", request.POST)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.save()
        if next_url != None:
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})
