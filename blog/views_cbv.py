from django.views.generic import CreateView
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # success_url = '/...' #원래 어디 url로 이동해준다 지정해줘야하는데 get_absolute_url()있으면 안해도 됨!

post_new = PostCreateView.as_view()
