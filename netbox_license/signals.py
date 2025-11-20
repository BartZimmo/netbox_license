from django.db.models.signals import pre_save
from django.dispatch import receiver
import logging

from netbox.context import current_request, events_queue
from extras.events import enqueue_event

from netbox_license.models import License

logger = logging.getLogger('netbox_license')

### This Signal is needed to trigger the Custom Event type.
### -> The Event type will be triggerd every time the Status field is updated from a License

@receiver(pre_save, sender=License)
def track_status_change(sender, instance, **kwargs):
    logger.debug("track_status_change signal loaded and triggered")
    logger.info("Signal triggered for License object")

    # Skip new objects (no previous state)
    if not instance.pk:
        return

    try:
        old_instance = License.objects.get(pk=instance.pk)
    except License.DoesNotExist:
        return

    # Check if status changed
    if old_instance.status != instance.status:
        logger.info(f"Status changed: {old_instance.status} -> {instance.status}")

        request = current_request.get()
        if request is None:
            logger.warning("No request context available; event not enqueued.")
            return

        queue = events_queue.get()
        try:
            enqueue_event(queue, instance, request, 'netbox_license.expirystatus')
            logger.info("Event enqueued: netbox_license.expirystatus")
        except Exception as e:
            logger.error(f"Failed to enqueue event: {e}")

        events_queue.set(queue)
