from django.urls import path

from . import views

app_name = 'laudo'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:documento_id>/', views.detail, name='detail'),
]