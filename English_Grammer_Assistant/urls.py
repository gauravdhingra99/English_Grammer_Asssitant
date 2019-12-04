from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'),name="accounts"),
    path('', TemplateView.as_view(template_name="index.html"),name="home"),
    path('assistant/', include('Assistant.urls'),name='check'),
]
