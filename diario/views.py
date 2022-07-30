from django.shortcuts import render
from .models import Post
from django.utils import timezone
import datetime

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'diario/post_list.html', {'posts': posts})