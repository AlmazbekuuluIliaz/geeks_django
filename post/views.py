from django.shortcuts import HttpResponse, render
from datetime import datetime
from post.models import Post
from .models import Product

# Create your views here.

#CBV - Class Based View
#FBV - Function Based View
#PEP8 - Python Enhancement Proposal 8

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")

def now_date_view(request):
    if request.method == 'GET':
        now_date = datetime.now()
        return HttpResponse(f"{now_date}")

def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")

def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all() #QuerySet
        # SELECT * from post_post;
        context = {
            "posts": posts,
        }
        return render(request, 'posts/posts.html')

def main_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        print(posts)
        return render(request, 'index.html')

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all() #QuerySet

        context = {
            "products": products
        }
        return render(request, 'products/products.html')

def hashtags_view(request):
    if request.method == 'GET':
        hashtags = HashTag.objects.all()

        context = {
            "hashtags": hashtags,
            "name": "Asyl"
        }

        return render(
            request,
            'posts/hashtags.html',
            context=context
        )

