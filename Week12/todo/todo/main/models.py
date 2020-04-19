from datetime import datetime
from django.db import models
from todo.auth_.models import MyUser
# from todo.utils.validators import validate_file_size, validate_extension


class ToDoListManager(models.Manager):

    def for_user(self, user):
        return self.filter(owner=user)

class ToDoManager(models.Manager):

    def for_list(self,todo_list):
        return self.filter(todo_list = todo_list)



class ToDoList(models.Model):
    name = models.CharField(max_length=40)
    img = models.ImageField(upload_to='todolist',
                              null=True, blank=True,
                             )
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    objects = ToDoListManager()

    class Meta:
        verbose_name = 'To Do List'
        verbose_name_plural = 'To Do lists'


    def __str__(self):
        return f'{self.name} todo list'


class ToDo(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now)
    due_on = models.DateTimeField(null=True, default=None)
    is_done = models.BooleanField(default=False)

    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='tasks')

    objects = ToDoListManager()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.name}, in {self.list}'

    # def set_status(self,value):
    #     self.is_done = value
    #     self.save()