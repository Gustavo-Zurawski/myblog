from django.urls import path

from myblog.blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]
