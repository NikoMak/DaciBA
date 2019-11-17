from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages

from .models import *
from .serializers import *

import json

# Create your views here.


# _____________________________________________________________________________________________________________________
# Log In and Out of page


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "tagcloud/login.html", {"message": "Ungültige Login Daten."})


def logout_view(request):
    logout(request)
    return render(request, "tagcloud/login.html", {"message": "Logged out."})

# _____________________________________________________________________________________________________________________
# Show Homepage


def index(request):
    current_user = request.user

    if not current_user.is_authenticated:
        return render(request, "tagcloud/login.html", {"message": None})

    projects = Project.objects.filter(topic__tag__user__username=current_user).distinct()
    topics = Topic.objects.filter(tag__user__username=current_user)
    tags = Tag.objects.filter(user__username=current_user)

    context = {
        'projects': projects,
        'tags': tags,
    }

    return render(request, 'tagcloud/index.html', context)

# _____________________________________________________________________________________________________________________
# Ajax Request


def ajax_get_topics(request):
    if request.method == "POST":
        current_user = request.user

        topics = Topic.objects.filter(tag__user__username=current_user).distinct()

        data = {
            'success': True,
            'topics': json.dumps(TopicSerializer(topics, many=True).data),
        }

        return JsonResponse(data, safe=False)

# _____________________________________________________________________________________________________________________
# Form submit


def tag_erfassen(request):
    if not request.user.is_authenticated:
        return render(request, "tagcloud/login.html", {"message": None})

    tag = request.POST['tag']
    topic = request.POST['topic']
    # project = request.POST['project']

    try:
        exists = Tag.objects.get(tag=tag, user=request.user)
        messages.success(request, tag + ' existiert bereits!')
        return HttpResponseRedirect(reverse("index"))
    except Tag.DoesNotExist:
        print('hello')
        new_tag = Tag(tag=tag, user=request.user)
        new_tag.save()

        upd_topic = Topic.objects.get(id=topic)
        upd_topic.tag.add(new_tag)

        messages.success(request, tag + ' wurde in der Datenbank erfasst!')
        return HttpResponseRedirect(reverse("index"))

