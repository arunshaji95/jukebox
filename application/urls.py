from django.urls import path

from application import views

app_name = 'application'

urlpatterns = [
    path('', views.ListUrls.as_view()),
]
