from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coach.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'coach_app.views.home', name='home'),
    url(r'^home', 'coach_app.views.home', name='home'),
    url(r'^results', 'coach_app.views.results', name='results'),
    url(r'^results2', 'coach_app.views.results2', name='results2'),
    url(r'^coach_home', 'coach_app.views.coach_home', name='coach_home'),
    url(r'^jan', 'coach_app.views.jan', name='jan'),


)
