from .models import Profile


def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
