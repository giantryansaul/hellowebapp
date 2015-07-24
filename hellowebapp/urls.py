from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)
from collection.backends import MyRegistrationView

urlpatterns = patterns('',
                       # Main pages
                       url(r'^$', 'collection.views.index',
                           name='home'),
                       url(r'^about/$', TemplateView.as_view(template_name='about.html'),
                           name='about'),
                       url(r'^contact/$', TemplateView.as_view(template_name='contact.html'),
                           name='contact'),

                       # Content
                       url(r'^hikes/$', RedirectView.as_view(pattern_name='browse')),
                       url(r'^hikes/(?P<slug>[-\w]+)/$', 'collection.views.hike_detail',
                           name='hike_detail'),
                       url(r'^hikes/(?P<slug>[-\w]+)/edit/$', 'collection.views.edit_hike',
                           name='edit_hike'),
                       url(r'^accounts/create_hike/$', 'collection.views.create_hike',
                           name="create_hike"),

                       # Browse Flow
                       url(r'^browse/$', RedirectView.as_view(pattern_name='browse')),
                       url(r'^browse/name/$', 'collection.views.browse_by_name',
                           name='browse'),
                       url(r'^browse/name/(?P<initial>[-\w]+)/$', 'collection.views.browse_by_name',
                           name='browse_by_name'),

                       # Registration pages
                       url(r'^accounts/password/reset/$', password_reset,
                           {'template_name': 'registration/password_reset_form.html'},
                           name="password_reset"),
                       url(r'^accounts/password/done/$', password_reset_done,
                           {'template_name': 'registration/password_reset_done.html'},
                           name="password_reset_done"),
                       url(r'^account/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
                           {'template_name': 'registration/password_reset_confirm.html'},
                           name="password_reset_confirm"),
                       url(r'^account/password/done/$', password_reset_complete,
                           {'template_name':'registration/password_reset_complete.html'},
                           name="password_reset_complete"),
                       url(r'^accounts/register/$', MyRegistrationView.as_view(),
                           name="registration_register"),
                       #url(r'^accounts/create_hike/$', 'collection.views.create_hike',
                       #    name="registration_create_hike"),
                       url(r'^accounts/create_profile/$', 'collection.views.create_profile',
                          name="registration_create_profile"),

                       # Accounts
                       url(r'^accounts/', include('registration.backends.simple.urls')),

                       # Profiles
                       url(r'^profiles/(?P<slug>[-\w]+)/$', 'collection.views.profile_detail',
                           name='profile_detail'),
                       url(r'^profiles/(?P<slug>[-\w]+)/edit/$', 'collection.views.edit_hike',
                           name='edit_profile'),

                       # Admin
                       url(r'^admin/', include(admin.site.urls))
)
