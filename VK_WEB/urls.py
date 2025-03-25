
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('ask', TemplateView.as_view(template_name='askForm.html'), name='ask'),
    path('question', TemplateView.as_view(template_name='question.html'), name='question'),
    path('tag/bander', TemplateView.as_view(template_name='tag.html'), name='tag'),
    path('settings', TemplateView.as_view(template_name='settings.html'), name='settings'),
    path('login', TemplateView.as_view(template_name='login.html'), name='login'),
    path('register', TemplateView.as_view(template_name='register.html'), name='register'),

]
