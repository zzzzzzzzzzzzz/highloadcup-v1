from django.forms.models import ModelForm

from visits.models import Visit


class PostForm(ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'
