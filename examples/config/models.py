from django.db import models
from solo.models import SingletonModel
from django.utils.translation import ugettext_lazy as _, ugettext as __


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(_('site name'), max_length=255, default='Site Name')
    maintenance_mode = models.BooleanField(_('maintenance mode'), default=False)

    def __str__(self):
        return __("Site Configuration")  # no proxy objects allowed here

    class Meta:
        verbose_name = _("Site Configuration")
