from django.shortcuts import render,redirect
from .forms import VideoForm
from .models import Videos
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
# Create your views here.
 



class VideoCreateView(CreateView):
    model = Videos
    form_class = VideoForm
    template_name = 'upload.html'
 



def display(request):
    
    post_list = Videos.objects.all().order_by('-time')
    paginator = Paginator(post_list, 6)
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
        
    
    return render(request, 'videos.html', context)