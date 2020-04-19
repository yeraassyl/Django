from todo.shop.models import Category, OnlineProduct

from todo.shop.serializers import CategorySerializer, OnlineProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, viewsets, generics
from django.http import Http404


class CategoryViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Category.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CategoryProductsAPIView(generics.ListCreateAPIView):
    serializer_class = OnlineProduct
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        try:
            category = Category.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except Category.DoesNotExist:
            raise Http404
        return category.products.all()

    def perform_create(self, serializer):
        try:
            category = Category.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except Category.DoesNotExist:
            raise Http404
        serializer.save(category=category)


class OnlineProductViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = OnlineProductSerializer
    permission_classes = (IsAuthenticated,)
    queryset = OnlineProduct.objects.all()