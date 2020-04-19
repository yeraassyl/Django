import logging

from todo.main.models import ToDoList,ToDo
from todo.main.serializers import ToDoListSerializer,ToDoSerializer,ToDoShortSerializer


from rest_framework import mixins, viewsets, generics
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated



logger = logging.getLogger(__name__)


class ToDoListViewSet(viewsets.ModelViewSet,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):

    permission_classes = (IsAuthenticated,)
    serializer_class = ToDoListSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def get_queryset(self):
        return ToDoList.objects.for_user(self.request.user)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        logger.debug(f'Created ToDoList,: {serializer.instance}')
        logger.info(f'Created ToDoList: {serializer.instance}')
        logger.warning(f'Created ToDoList,: {serializer.instance}')
        logger.error(f'Created ToDoList, : {serializer.instance}')
        logger.critical(f'Created ToDoList: {serializer.instance}')


    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
        logger.info(f'Updated ToDoList: {serializer.instance}')


    def perform_destroy(self, instance):
        instance.delete()
        logger.info(f'Deleted ToDoList: {instance}')



class ToDoViewSet(viewsets.ModelViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet
                  ):

    permission_classes = (IsAuthenticated,)
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()


    def get_queryset(self):
        return ToDo.objects.for_list(self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ToDoSerializer
        return ToDoShortSerializer

    def perform_create(self, serializer):
        list_id = self.kwargs.get('parent_lookup_list')
        serializer.save(list=ToDoList.objects.get(id=list_id))


