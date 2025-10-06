from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import CSMediaProfile, CSMediaRelationship

@receiver(post_save, sender=User)
def profile_creation_post_save(sender, instance, created, **kwargs):
    print('sender', sender) #edit
    print('instance', instance) #edit
    if created:
        CSMediaProfile.objects.create(csmedia_user=instance)

@receiver(post_save, sender=CSMediaRelationship)
def friend_request_post_save(sender, instance, created, **kwargs):
    request_sender = instance.friend_request_sender
    request_receiver = instance.friend_request_receiver
    if instance.friend_request_status == 'accepted':
        request_sender.user_friends.add(request_receiver.csmedia_user)
        request_receiver.user_friends.add(request_sender.csmedia_user)
        request_sender.save()
        request_receiver.save() 