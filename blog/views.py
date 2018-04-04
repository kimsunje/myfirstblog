from django.shortcuts import render
from .models import Post 
# models.py 가져옴 같은 디렉토리에 위치하고 있기 때문에 . 으로 명시 
from django.utils import timezone
# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts':posts})