from django.urls import path

from todo.main.views import ToDoListsView, ToDoListView, ToDosView, ToDoView

# urlpatterns = [
#     path('', ToDoListsView.as_view()),
#     path('<int:pk>/', ToDoListView.as_view()),
#     path('<int:pk>/todo/', ToDosView.as_view()),
#     path('<int:pk2>/todo/<int:pk>/', ToDoView.as_view()),
# ]

from todo.main.viewsets import ToDoListViewSet,ToDoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


router.register(r'lists',ToDoListViewSet,basename='lists')
router.register(r'tasks',ToDoViewSet,basename='tasks')


urlpatterns = router.urls
