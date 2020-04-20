from django.core.management.base import BaseCommand
from datetime import datetime
import random

from todo.main.models import ToDoList, ToDo


class Command(BaseCommand):
    help = 'Delete ToDo List objects from table'

    def add_arguments(self, parser):
        parser.add_argument('todo_ids', nargs='+', help='todo ids for delete')

    def handle(self, *args, **kwargs):

        for todo_id in kwargs['todo_ids']:
            try:
                t = ToDoList.objects.get(id=todo_id)
                t.delete()
                self.stdout.write(self.style.SUCCESS(f"ToDo List id: {todo_id} was deleted successfully"))
            except ToDoList.DoesNotExist as e:
                self.stdout.write(self.style.ERROR(f"ToDo List id: {todo_id} does not exists!"))