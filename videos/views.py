from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VideoUploadForm

# Create your views here.


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