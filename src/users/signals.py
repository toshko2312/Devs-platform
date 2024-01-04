from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

from users.models import Profile


def createProfile(sender, instance: User, created: bool, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
            name=instance.first_name
        )


def deleteUser(sender, instance: Profile, **kwargs):
    instance.user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
