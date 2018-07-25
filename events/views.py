import os

from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from application.models import Link

SLACK_VERIFICATION_TOKEN = os.environ.get('SLACK_VERIFICATION_TOKEN', '')


class Events(APIView):
    """
    API for handling slack events.
    """
    def post(self, request, *args, **kwargs):
        slack_message = request.data
        if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)
        # Verification Challenge
        if slack_message.get('type') == 'url_verification':
            return Response(data=slack_message,
                            status=status.HTTP_200_OK)
        try:
            channel = slack_message['event']['channel']
            if channel == settings.SLACK_CHANNEL:
                self.process_message(slack_message)
        except KeyError:
            pass
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def process_message(message):
        try:
            attachments = message['event']['message']['attachments']
        except KeyError:
            return
        for attachment in attachments:
            if attachment['service_name'] == 'YouTube':
                url = attachment['title_link']
                link, created = Link.objects.get_or_create(url=url)
