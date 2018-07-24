from django.urls import path

from events import views

app_name = 'events'

urlpatterns = [
    path('', views.Events.as_view()),
]
