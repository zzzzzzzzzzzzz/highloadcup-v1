from django.forms.models import ModelForm

from locations.models import Location


class PostForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

