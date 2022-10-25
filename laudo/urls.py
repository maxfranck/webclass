from django.urls import path
from .views import redirect_admin, redirect_laudo
from . import views

app_name = 'laudo'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:documento_id>/', views.detail, name='detail'),
    path('admin/laudo/documento/', views.amostras, name='amostras'),
    path('admin/', redirect_admin, name='redirect_admin'),
    path('admin/laudo/', redirect_laudo, name='redirect_laudo'),
]