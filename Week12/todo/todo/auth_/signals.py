from django.db.models.signals import post_save
from django.dispatch import receiver

from todo.auth_.models import MyUser,Profile
from todo.main.models import ToDoList


@receiver(post_save, sender=MyUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        ToDoList.objects.create(owner=instance)




# @receiver(post_save, sender=MyUser)
# def user_created(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)