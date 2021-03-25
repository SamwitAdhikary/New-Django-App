from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog(request):
    all_posts = Paginator(Post.objects.filter(published=True).order_by('-timestamp'), 6)
    page = request.GET.get('page')
    try:
        allPosts = all_posts.page(page)
    except PageNotAnInteger:
        allPosts = all_posts.page(1)
    except EmptyPage:
        allPosts = all_posts.page(all_posts.num_pages)

    context = {'allPosts': allPosts}
    return render(request, 'blog/blog.html', context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/blogpost.html', context)