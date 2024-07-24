from django.shortcuts import render, redirect
from .models import Post, Contact, Comment, Information
from users.models import CustomUser
import requests
from decouple import config
from django.core.paginator import Paginator
# Create your views here.
def base(request, username):
    info = Information.objects.all().first()
    user = CustomUser.objects.get(username=username)
    context = {
        "user": user,
        "info": info,
    }
    return render(request, 'base.html', context=context)


def home(request):
    posts = Post.objects.all().filter(is_published=True).order_by("-view_count")[:6]
    context = {
        "posts": posts,
        "home": "active",
    }
    return render(request, "index.html", context=context)


def blog(request):
    data = request.GET
    ctg = data.get('ctg', None)
    page = data.get('page', 1)
    if ctg:
        posts = Post.objects.all().filter(is_published=True, category__slug=ctg)
        context = {
            "posts": posts,
            "blog": "active",
        }
        return render(request, 'blog.html', context=context)

    posts = Post.objects.all().filter(is_published=True)
    page_obj = Paginator(posts , 9)

    context = {
        "posts":page_obj.get_page(page),
        "blog": "active",
    }
    return render(request, 'blog.html', context=context)


def blog_detail(request, slug):
    post = Post.objects.filter(is_published=True).get(slug=slug)
    if request.method == "POST":
        data = request.POST
        comment = Comment.objects.create(user=post.user, post=post, message=data['message'])
        comment.save()

        return redirect(f"/blog/{slug}/")

    comments = Comment.objects.filter(is_public=True, post=post)
    post.view_count += 1
    post.save(update_fields=["view_count"])
    context = {
        "post": post,
        "comments": comments,
        "blog": "active",
    }
    return render(request, 'blog-single.html', context=context)


def about(request):
    context = {
        "about": "active"
    }
    return render(request, 'about.html', context=context)


def contact(request):
    if request.method == "POST":
        data = request.POST
        contact = Contact.objects.create(name=data['name'], email=data['email'], subject=data['subject'],
                                         message=data['message'])
        contact.save()
        message = (f"Project : Moose.uz\nID : {contact.id}\nUser : {contact.name}\nEmail :  {contact.email}\nSubject : "
                   f"{contact.subject}\nMessage : {contact.message}\nTime : {contact.created_at.date()}  // "
                   f" {contact.created_at.hour}:{contact.created_at.minute}:{contact.created_at.second}")
        BOT_TOKEN = config("BOT_TOKEN")
        CHAT_ID = config("CHAT_ID")
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        response = requests.get(url)
        print(response)
        return redirect("/contact")

    info = Information.objects.all().first()
    context = {
        "info": info,
        "contact": "active",
    }
    return render(request, 'contact.html', context=context)
