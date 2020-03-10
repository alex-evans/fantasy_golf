from django.contrib import admin
from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tournament_view, name='current_tournament')
]
