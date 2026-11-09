from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VideoUploadForm
from .models import Video
from django.shortcuts import render, redirect, get_object_or_404
from .models import Video

# Create your views here.

def home(request):
    videos=Video.objects.select_related('uploaded_by').order_by('-uploaded_at')
    return render(request,'videos/home.html',{'videos': videos})
    
    
@login_required(login_url='login')
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST,request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploaded_by = request.user
            video.save()
            return redirect('profile',username=request.user.username)
    else:
        form = VideoUploadForm()
    return render(request,'videos/upload.html',{'form': form})

def watch_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.views += 1
    video.save(update_fields=['views'])
    return render(request,'videos/watch.html',{'video': video})