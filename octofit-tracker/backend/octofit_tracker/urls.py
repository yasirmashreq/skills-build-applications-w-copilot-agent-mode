"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tracker.views import api_root
import os
from django.http import HttpRequest

class CodespaceHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.codespace_name = os.environ.get('CODESPACE_NAME')
        self.codespace_host = f"{self.codespace_name}-8000.app.github.dev" if self.codespace_name else None

    def __call__(self, request: HttpRequest):
        if self.codespace_host:
            request.META['HTTP_HOST'] = self.codespace_host
            request.scheme = 'https'
        return self.get_response(request)

def codespace_host_middleware(get_response):
    return CodespaceHostMiddleware(get_response)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include('tracker.urls')),
]
