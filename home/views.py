from django.db.models import query
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Contact
from blog.models import Post
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    allPosts = Post.objects.filter(published=True).order_by('-timestamp')
    context = {'allPosts': allPosts}
    return render(request, 'home/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request, 'home/contact.html')

def search(request):
    posts_list = Post.objects.all()
    query = request.GET.get('query')
    if query:
        posts_list = Post.objects.filter(
            Q(title__icontains=query) | Q(short_desc__icontains=query)
        ).distinct()
    
    paginator = Paginator(posts_list, 6)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    params = {'posts': posts, 'query': query}
    return render(request, 'home/search.html', params)

