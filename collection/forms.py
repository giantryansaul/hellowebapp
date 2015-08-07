from django.forms import ModelForm

from collection.models import Hike, Profile

class HikeForm(ModelForm):
    class Meta:
        model = Hike
        fields = (
            'name',
            'description',
            'region'
        )

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'bio'
        )