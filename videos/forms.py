from django import forms
from .models import Video


class VideoUploadForm(forms.ModelForm):

    class Meta:
        model = Video

        fields = [
            'title',
            'description',
            'video_file',
            'thumbnail',
            'category'
        ]
        
    def clean_video_file(self):

        video = self.cleaned_data.get('video_file')

        if video:

            allowed_extensions = [
                '.mp4',
                '.webm',
                '.mov'
            ]

            import os

            extension = os.path.splitext(video.name)[1].lower()

            if extension not in allowed_extensions:
                raise forms.ValidationError('Unsupported video format.')

            if video.size > 100 * 1024 * 1024:
                raise forms.ValidationError('Video cannot exceed 100MB.')

        return video