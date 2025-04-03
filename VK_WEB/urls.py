
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app import views
urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('ask', views.askForm, name='ask'),
    path('question', views.question, name='question'),
    path('tag/bander', views.tag, name='tag'),
    path('settings', views.settings, name='settings'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

]
