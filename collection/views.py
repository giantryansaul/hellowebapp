from django.shortcuts import render, redirect
from collection.forms import HikeForm
from collection.models import Hike


# Create your views here.
def index(request):
    hikes = Hike.objects.all().order_by('name')
    return render(request, 'index.html', {'hikes': hikes}, )


def hike_detail(request, slug):
    hike = Hike.objects.get(slug=slug)
    return render(request, 'hikes/hike_detail.html', {'hike': hike, })


def edit_hike(request, slug):
    hike = Hike.objects.get(slug=slug)
    form_class = HikeForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=hike)
        if form.is_valid():
            form.save()
            return redirect('hike_detail', slug=hike.slug)
    else:
        form = form_class(instance=hike)

    return render(request, 'hikes/edit_hike.html', {'hike': hike, 'form': form, })