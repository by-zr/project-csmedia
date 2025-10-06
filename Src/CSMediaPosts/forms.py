from django import forms
from .models import CSMediaPost, CSMediaComment

class CSMediaPostForm(forms.ModelForm):
    post_content = forms.CharField(widget=forms.Textarea(attrs={'rows':2})) #edit again
    class Meta:
        model = CSMediaPost
        fields = ('post_content', 'post_image')

class CSMediaCommentForm(forms.ModelForm):
    comment_body = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Sending some love ...'}))
    class Meta:
        model = CSMediaComment
        fields = ('comment_body',)





   