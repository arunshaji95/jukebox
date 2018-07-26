from django.views.generic import ListView

from .models import Link


class ListUrls(ListView):
    model = Link
