
from todo.main.models import ToDoList,ToDo
from todo.main.serializers import ToDoListSerializer,ToDoSerializer,ToDoShortSerializer


from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated

import logging


logger = logging.getLogger(__name__)


class ToDoListViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return ToDoList.objects.for_user(self.request.user)

    permission_classes = (IsAuthenticated,)
    serializer_class = ToDoListSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        logger.info(f'Created ToDoList: {serializer.instance}')


    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'Updated ToDoList: {serializer.instance}')


    def perform_destroy(self, instance):
        instance.delete()
        logger.info(f'Deleted ToDoList: {instance}')



class ToDoViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        return ToDo.objects.filter(list=self.kwargs.get('parent_lookup_list'))


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ToDoSerializer
        return ToDoShortSerializer

    def perform_create(self, serializer):
        list_id = self.kwargs.get('parent_lookup_list')
        serializer.save(list=ToDoList.objects.get(id=list_id))


