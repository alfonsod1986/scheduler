from datetime import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Property
from .constants import DISABLED, LOCAL_TZ

@receiver(pre_save, sender=Property)
def PropertyUpdate(sender, instance, *args, **kwargs):
    if instance.status == DISABLED:
        instance.disabled_at = LOCAL_TZ.localize(datetime.now()) 