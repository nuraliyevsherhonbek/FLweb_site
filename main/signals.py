from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Application
from django.conf import settings
from main.views import bot


@receiver(signal=post_save, sender=Application)
def send_application(sender, instance, **kwargs):
    first_name = instance.first_name
    last_name = instance.last_name
    subject = instance.subject
    phone_number = instance.phone_number
    text = f"<b>{first_name} {last_name}</b> \n {subject} \n {phone_number}"
    bot.send_message(settings.CHAT_ID, text, parse_mode='HTML')

