from django.conf.urls import url
from . import views
from django.urls.conf import path, re_path

app_name = 'message'
urlpatterns = [
    # re_path(r'^submit-comment/$', views.submit_message, name='submit_message'),
    path('messages/', views.submit_message, name='submit_message'),
    path('delete_message/', views.delete_message, name='delete_message'),
    path('hide_message/', views.hide_message, name='hide_message'),
    path('public_message/', views.public_message, name='public_message'),
]

