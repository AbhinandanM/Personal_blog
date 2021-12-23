
from django import forms
from .models import Post, Category, Author, Comment, AdmMessage, img_categories
from captcha.fields import ReCaptchaField


choice = img_categories.objects.all().values_list('name', 'name')


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField(
        public_key='6Lc0cM4ZAAAAAMV1S2pWIRx6o-83lKXeV9I4gJ9r',
        private_key='6Lc0cM4ZAAAAAJUz-yxNAQn8pu2hTh5iyuzjQ9mR',
    )

    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {

            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your comment:', 'rows': '6'})

        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail', 'featured',
                  'categories', 'img_category', 'previous_post', 'next_post')

        widgets = {
            'img_category': forms.Select(choices=choice),




        }


class MessageForm(forms.ModelForm):

    class Meta:
        model = AdmMessage
        fields = ('title', 'title_tag')
