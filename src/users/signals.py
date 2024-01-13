from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
from django.conf import settings

from users.models import Profile


def create_profile(sender, instance: User, created: bool, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
            name=instance.first_name
        )

        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!!!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )


def update_user(sender, instance: Profile, created, **kwargs):
    user: User = instance.user
    if not created:
        user.first_name = instance.name
        user.username = instance.username
        user.email = instance.email
        user.save()


def delete_user(sender, instance: Profile, **kwargs):
    instance.user.delete()


post_save.connect(create_profile, sender=User)
post_save.connect(update_user, sender=Profile)
post_delete.connect(delete_user, sender=Profile)
