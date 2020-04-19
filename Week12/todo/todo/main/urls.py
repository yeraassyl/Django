from django.urls import path

from todo.main.cbv import ToDoListsView, ToDoListView, ToDosView, ToDoView

# urlpatterns = [
#     path('', ToDoListsView.as_view()),
#     path('<int:pk>/', ToDoListView.as_view()),
#     path('<int:pk>/todo/', ToDosView.as_view()),
#     path('<int:pk2>/todo/<int:pk>/', ToDoView.as_view()),
# ]

from todo.main.views import ToDoListViewSet,ToDoViewSet
from rest_framework.routers import DefaultRouter

# from rest_framework_extensions.routers import ExtendedSimpleRouter
# from todo.main.viewsets import ToDoListViewSet, ToDoViewSet
#
#
# router.register(r'task_lists', TaskListViewSet, basename='tasks-lists').\
#     register(r'tasks', TaskViewSet, basename='tasks', parents_query_lookups=['task_list'])
#
# urlpatterns = router.url

# router = DefaultRouter()
#
#
# router.register(r'lists',ToDoListViewSet,basename='lists')
# router.register(r'tasks',ToDoViewSet,basename='tasks')

#
# urlpatterns = router.urls

from rest_framework_extensions.routers import ExtendedSimpleRouter
from todo.main.views import ToDoViewSet, ToDoListViewSet

router = ExtendedSimpleRouter()

router.register(r'lists', ToDoListViewSet, basename='tasks-lists').\
    register(r'tasks', ToDoViewSet, basename='tasks', parents_query_lookups=['task_list'])

urlpatterns = router.urls