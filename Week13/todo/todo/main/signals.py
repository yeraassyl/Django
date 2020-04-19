from django.db.models.signals import post_save
from django.dispatch import receiver

from todo.main.models import ToDoList,ToDo


@receiver(post_save, sender = ToDoList)
def todolist_created(sender,instance,created, **kwargs ):
    if created:
        todo_list = instance.list
        if todo_list.task_amount is None:
            ToDoList.objects.filter(id=todo_list.id) \
                .update(task_amount=ToDoList.objects.get(id=todo_list.id).todo_set.count())
        else:
            ToDoList.objects.filter(id=todo_list.id).update(task_amount=todo_list.task_amount + 1)