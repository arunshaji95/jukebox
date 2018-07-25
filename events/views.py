import os

from django.conf import settings
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response

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
        print("Inside process_message")
        # TODO: implement logic for parsing message
        pass
