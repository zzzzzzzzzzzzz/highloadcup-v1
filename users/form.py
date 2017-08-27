from django.forms.models import ModelForm

from users.models import User


class PostForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'