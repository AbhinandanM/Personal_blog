from django import forms
from video_content.models import Videos



class VideoForm(forms.ModelForm):

    class Meta:
        model = Videos
        fields = ('title', 'video')