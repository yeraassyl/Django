from django.http import Http404
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated

from todo.main.models import ToDoList,ToDo
from todo.main.serializers import ToDoListSerializer,ToDoSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action


class ToDoListViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)


    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer


class ToDoViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)

    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


    @action(methods=['PUT'],detail=True)
    def set_status(self,request):
        todo = self.get_object()
        todo.set_status(request.data.get('value'))
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)




