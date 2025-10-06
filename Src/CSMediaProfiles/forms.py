from django import forms
from.models import CSMediaProfile

class CSMediaProfileForm(forms.ModelForm):
    class Meta:
        model = CSMediaProfile
        fields = ('first_name', 'last_name', 'user_bio', 'user_avatar')