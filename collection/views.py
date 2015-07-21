from django.shortcuts import render
from collection.models import Hike


# Create your views here.
def index(request):
    hikes = Hike.objects.all().order_by('name')
    return render(request, 'index.html', {'hikes': hikes}, )


def hike_detail(request, slug):
    hike = Hike.objects.get(slug=slug)
    return render(request, 'hikes/hike_detail.html', {'hike': hike, })