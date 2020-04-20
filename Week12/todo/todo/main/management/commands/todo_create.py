from django.core.management.base import BaseCommand
from datetime import datetime
import random
from todo.main.models import ToDoList,ToDo
from todo.auth_.models import MyUser



class Command(BaseCommand):
    """
        Creates random object in databases, before it optionally drop database
        """

    help = 'Create random lists and todo elements'

    def add_arguments(self, parser):
        parser.add_argument('-o', '--owner', type=int, help='Id of owner of lists')
        parser.add_argument('-d', '--drop', action='store_true', help='Flag if drop all before creating objects')

    def handle(self, *args, **options):

        owner_id = options.get('owner')
        try:
            owner = MyUser.objects.get(id=owner_id)
        except:
            self.stdout.write(self.style.ERROR(f'User with id {owner_id} now found'))
            return

        if options.get('drop'):
            ToDoList.objects.all().delete()
            ToDo.objects.all().delete()

            self.stdout.write(self.style.WARNING(f'All Todo list and todo objects dropped'))

        num = random.randint(1, 10)
        lists = []

        # Create lists
        for i in range(num):
            listt = ToDoList.objects.create(name=f'list {i}', owner=owner)

            lists.append(listt)

            self.stdout.write(self.style.SUCCESS(f'Todo list {listt.id} created'))
