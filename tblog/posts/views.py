from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Posts, PostImage

def img_view(request):
    posts = Posts.objects.all().order_by('-time_ago')
    paginator = Paginator(posts, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)



    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        
    }
    return render(request, 'gallery.html', context)

def detail_view(request, id):
    post = get_object_or_404(Posts, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {
        'post':post,
        'photos':photos
    })

def create_post_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        post = Posts.objects.create(
            title=title,
            description=description
        )
        
        for file_num in range(0, int(length)):
            PostImage.objects.create(
                post=post,
                images=request.FILES.get(f'images{file_num}')
            )


    return render(request, 'create-post.html')