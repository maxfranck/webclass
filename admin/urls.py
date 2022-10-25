from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('laudo.urls')),
    path('admin/', admin.site.urls),
]
admin.site.site_header = "Nucoffee"
admin.site.site_title = "Nucoffee"
admin.site.index_title = "Webclass"