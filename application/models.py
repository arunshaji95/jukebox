from django.db import models
from django.utils.translation import gettext_lazy as _


class Link(models.Model):
    """
    Model for storing youtube links.
    """
    url = models.URLField(_('url'), unique=True)
    votes = models.PositiveIntegerField(_('votes'), default=0)
    created = models.DateTimeField(_('created at'), auto_now_add=True)
    last_updated = models.DateTimeField(_('laste updated'), auto_now=True)

    def __str__(self):
        return '{} with {} votes'.format(self.url, self.votes)
