from django.shortcuts import render, redirect
from django.template import RequestContext
from collection.forms import HikeForm
from collection.models import Hike
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    hikes = Hike.objects.all().order_by('name')
    return render(request, 'index.html', {'hikes': hikes}, )


def hike_detail(request, slug):
    hike = Hike.objects.get(slug=slug)
    return render(request, 'hikes/hike_detail.html', {'hike': hike, })


@login_required
def edit_hike(request, slug):
    hike = Hike.objects.get(slug=slug)

    if hike.user != request.user:
        raise Http404

    form_class = HikeForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=hike)
        if form.is_valid():
            form.save()
            return redirect('hike_detail', slug=hike.slug)
    else:
        form = form_class(instance=hike)

    return render(request, 'hikes/edit_hike.html', {'hike': hike, 'form': form, })


def create_hike(request):
    user = request.user
    form_class = HikeForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            slug = slugify(name)

            hike = Hike.objects.create(
                name=name,
                description=description,
                slug=slug,
                user=user
            )

        return redirect('hike_detail', slug=hike.slug)

    else:
        form = form_class()

    return render(request, 'hikes/create_hike.html', { 'form': form, },
                  context_instance=RequestContext(request))