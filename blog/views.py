from django.shortcuts import render
from .models import Post ,Contact , Category , Comment

# Create your views here.
def home(request):
    context = {

    }
    return render(request , "index.html", context=context)

def blog(request):
    posts = Post.objects.all().filter(is_published=True)

    context = {
        "posts":posts,
    }
    return render(request , 'blog.html', context=context)

def blog_detail(request, pk):
    if request.POST:
        data = request.POST
        obj = Comment.objects.create(name = data['name'] , email=data['email'] , message=data['message'])
        obj.save()

        return obj

    post = Post.objects.filter(is_published=True).get(pk=pk)
    categories = Category.objects.all()
    comments = Comment.objects.all().filter(is_public=True)
    context = {
        "post":post,
        "categories":categories,
        "comments":comments,
    }
    return render(request , 'blog-single.html' , context=context)

def about(request):
    context = {

    }
    return render(request , 'about.html' , context=context)

def contact(request):
    if request.POST:
        data = request.POST
        obj = Contact.objects.create(full_name=data['name'],email=data['email'], subject=data['subject'],
                                     message=data['message'])
        obj.save()

        return obj

    context = {

    }
    return render(request , 'contact.html', context=context)