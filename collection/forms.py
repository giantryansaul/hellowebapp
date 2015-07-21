from django.forms import ModelForm

from collection.models import Hike

class HikeForm(ModelForm):
    class Meta:
        model = Hike
        fields = ('name', 'description')