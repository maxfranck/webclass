from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('laudo.urls')),
    path('admin/', admin.site.urls),
]
admin.site.site_header = "Nucoffee"
admin.site.site_title = "Nucoffee"
admin.site.index_title = "Webclass"