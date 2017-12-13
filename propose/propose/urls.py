"""propose URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django.views import generic
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^$', generic.TemplateView.as_view(template_name='view1.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^view2/', generic.TemplateView.as_view(template_name='view2.html')),
    url(r'^freelancer_search/', generic.TemplateView.as_view(template_name='freelancer_search.html')),
    url(r'^project_search/', generic.TemplateView.as_view(template_name='project_search.html')),
    url(r'^client_project_view/', generic.TemplateView.as_view(template_name='client_project_view.html')),
    url(r'^api/', include('account.urls', namespace='account')),
    url(r'^api/', include('application.urls', namespace='application')),
    url(r'^api/', include('dashboard.urls', namespace='dashboard')),
    url(r'^api/', include('project.urls', namespace='project')),
    url(r'^api/', include('tag.urls', namespace='tag')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
