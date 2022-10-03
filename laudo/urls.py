from django.urls import path

from . import views

urlpatterns = [
    # ex: /laudo/
    path('', views.index, name='index'),
    # ex: /laudo/5/
    path('<int:laudo_id>/', views.detail, name='detail'),
]