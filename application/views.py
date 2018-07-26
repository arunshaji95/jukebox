from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, View
from django.urls import reverse
from .models import Link


class ListUrls(View):
    def get(self, request, *args, **kwargs):
        context = {
            'object_list': Link.objects.all()
        }
        return render(request, 'application/link_list.html', context)

    def post(self, request, *args, **kwargs):
        if not request.POST.get('video'):
            return HttpResponseRedirect(reverse('application:home'))
        link_id = request.POST['video']
        try:
            link = Link.objects.get(pk=link_id)
            link.votes += 1
            link.save()
        except Link.DoesNotExist:
            raise Http404
        return HttpResponseRedirect(reverse('application:home'))


class VoteView(FormView):
    pass
