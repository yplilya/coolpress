from django.http import HttpResponse
from django.shortcuts import render
from coolpress.press.models import Post


def index(request):
    return HttpResponse('Hi this is my first app')

def post_detail(request, post_id):
    post_object = Post.objects.get(pk=post_id)

    return HttpResponse(f'''The asked post is: {post_object}''')