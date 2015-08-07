from django.shortcuts import render, redirect
from django.template import RequestContext
from collection.forms import HikeForm, ProfileForm
from collection.models import Hike, Profile
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    hikes = Hike.objects.all().order_by('name')
    latest_hikes = Hike.objects.all().order_by('-id')[:3][::-1]
    return render(request, 'index.html', {'hikes': hikes, 'latest': latest_hikes})


def user_profile(request):
    profile = request.user.profile
    return render(request, 'profiles/profile_detail.html', {'profile': profile, })


def profile_detail(request, slug):
    profile = Profile.objects.get(slug=slug)
    return render(request, 'profiles/profile_detail.html', {'profile': profile, })


@login_required
def edit_profile(request, slug):
    profile = Profile.objects.get(slug=slug)

    if profile.user != request.user:
        raise Http404

    form_class = ProfileForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', slug=profile.slug)
    else:
        form = form_class(instance=profile)

    return render(request, 'profiles/edit_profile.html', {
        'profile': profile,
        'form': form,
    })


def create_profile(request):
    user = request.user
    form_class = ProfileForm

    if request.method == 'POST':
        profile = None
        form = form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            bio = form.cleaned_data['bio']

            slug = slugify("{0} {1}".format(first_name, last_name))

            profile = Profile.objects.create(
                first_name=first_name,
                last_name=last_name,
                bio=bio,
                slug=slug,
                user=user
            )

        return redirect('profile_detail', slug=profile.slug)

    else:
        form = form_class()

    return render(request, 'profiles/create_profile.html', {
        'form': form,
    }, context_instance=RequestContext(request))


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

    return render(request, 'hikes/edit_hike.html', {
        'hike': hike,
        'form': form,
    })


def create_hike(request):
    user = request.user
    form_class = HikeForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            region = form.cleaned_data['region']

            slug = slugify(name)

            hike = Hike.objects.create(
                name=name,
                description=description,
                slug=slug,
                user=user,
                region=region
            )

            return redirect('hike_detail', slug=hike.slug)

    else:
        form = form_class()

    return render(request, 'hikes/create_hike.html', {
        'form': form,
    }, context_instance=RequestContext(request))


def browse_by_name(request, initial=None):
    if initial:
        hikes = Hike.objects.filter(name__istartswith=initial).order_by('name')
    else:
        hikes = Hike.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'hikes': hikes,
        'initial': initial
    })