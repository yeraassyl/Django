from datetime import datetime
from django.db import models
from todo.auth_.models import MyUser
from todo.main.validators import validate_file_size, validate_extension


class ToDoListManager(models.Manager):

    def for_user(self, user):
        return self.filter(owner=user)

class ToDoManager(models.Manager):

    def for_list(self,todo_list):
        return self.filter(todo_list = todo_list)


class ToDoList(models.Model):
    name = models.CharField(max_length=40)
    img = models.ImageField(upload_to='todolist',
                            validators=[validate_file_size,validate_extension],
                            null=True, blank=True,
                            )

    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    objects = ToDoListManager()

    class Meta:
        verbose_name = 'ToDo List'
        verbose_name_plural = 'ToDo Lists'


    def __str__(self):
        return f'{self.name} todo list'


class ToDoBase(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class ToDo(ToDoBase):
    created_at = models.DateTimeField(default=datetime.now)
    due_on = models.DateTimeField(null=True, default=None)
    is_done = models.BooleanField(default=False)

    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='tasks')

    objects = ToDoManager()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.name}, in {self.list}'

    # def set_status(self,value):
    #     self.is_done = value
    #     self.save()