from rest_framework.routers import DefaultRouter

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


from rest_framework_extensions.routers import ExtendedSimpleRouter
from todo.main.views.viewsets import ToDoViewSet, ToDoListViewSet

router = ExtendedSimpleRouter()

router.register(r'lists', ToDoListViewSet, basename='tasks-lists').\
    register(r'tasks', ToDoViewSet, basename='tasks',
             parents_query_lookups=['task_list']
             )

urlpatterns = router.urls