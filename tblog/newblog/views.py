from django.shortcuts import render,  get_object_or_404, redirect, reverse
from .models import Post, Category, Author, Comment, PostViewCount, AdmMessage, img_categories
from marketing.models import SignUP
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from .forms import CommentForm, PostForm, MessageForm
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.
import re


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_result.html', context)


def get_category_count():
    queryset = Post.objects.values(
        'categories__title').annotate(Count('categories__title'))
    return queryset


def index(request):
    featured_post = Post.objects.filter(featured=True).order_by('-timestamp')[0:6]
    adminmessage = AdmMessage.objects.order_by('-timestamps')
    latest = Post.objects.order_by('-timestamp')[0:6]
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    post_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(post_list, 15)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = SignUP()
        new_signup.email = email
        new_signup.save()

    context = {
        'featured_post': featured_post,
        'object_list': adminmessage,
        'latest': latest,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'most_recent': most_recent,
        'category_count': category_count
    }
    return render(request, 'main.html', context)


def post(request, id, title):
    user = request.user
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    post = get_object_or_404(Post, id=id)
    if user.is_authenticated:
        PostViewCount.objects.create(user=request.user, post=post)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={'id': post.id, 'title': post.title}))

    context = {
        'post': post,
        'most_recent': most_recent,
        'category_count': category_count,
        'form': form
    }
    return render(request, 'post.html', context)


def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if (request.method == "POST"):
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={'id': form.instance.id}))

    context = {
        'title': title,

        'form': form
    }

    return render(request, "post_create.html", context)


def post_update(request, id):
    title = 'Update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user)
    if (request.method == "POST"):
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={'id': form.instance.id}))

    context = {

        'title': title,

        'form': form
    }

    return render(request, "post_create.html", context)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("post-list"))


class MessageCreateView(CreateView):
    model = AdmMessage
    form_class = MessageForm
    template_name = 'create_message.html'


class MessageUpdateView(UpdateView):
    model = AdmMessage
    template_name = 'update-message.html'
    fields = '__all__'


def about(request):
    return render(request, 'about_us.html', {})


class AddImg_categoryView(CreateView):
    model = img_categories
    template_name = 'add_category.html'
    fields = '__all__'


def Img_categoryView(request, cates):
    category_posts = Post.objects.filter(
        img_category=cates).order_by('-timestamp')
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    paginator = Paginator(category_posts, 15)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'cates': cates.title(),
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'most_recent': most_recent,
        'category_count': category_count,
        'category_posts': category_posts
    }

    return render(request, 'img-categories.html', context)


def Img_categoryListView(request, *args, **kwargs):
    cat_list = img_categories.objects.all()
    return render(request, 'img-categories_list.html', {'cat_list': cat_list})
