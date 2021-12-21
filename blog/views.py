from django.conf import settings
from django.shortcuts import render

from .utils import read_json_file


def index(request):
    template_name = 'blog/index.html'
    index_json_file = (
        settings.BASE_DIR / 'blog' / 'content' / 'index_content.json'
    )
    index_content = read_json_file(index_json_file)
    context = {
        'posts': index_content
    }
    return render(request, template_name, context)


def post(request):
    template_name = 'blog/post.html'
    index_json_file = (
        settings.BASE_DIR / 'blog' / 'content' / 'post_content.json'
    )
    post_content = read_json_file(index_json_file)
    context = {
        'post': post_content
    }
    return render(request, template_name, context)
