"""probes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import table
from web import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = [
#    url(r'^test', TemplateView.as_view(template_name="test.html")),
    url("", include('django_socketio.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^table/', include('table.urls')),
    url(r'^get_data', login_required(views.get_data), name='get_data'),
    url(r'^probe_data', login_required(views.probe_data), name='probe_handler'),
    url(r'^$', login_required(TemplateView.as_view(template_name="base.html")), name='overview'),
    url(r'^probe_table', login_required(views.table), name='probe_table'),
    url(r'^location_plot', login_required(views.location_plot), name='location_plot'),
    url(r'^probe_graph', login_required(views.probe_graph), name='probe_graph'),
    url(r'^table/data/$', login_required(views.ProbeDataView.as_view()), name='table_data'),
]
