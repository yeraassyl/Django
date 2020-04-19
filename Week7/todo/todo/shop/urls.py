
from todo.shop.views import CategoryViewSet,OnlineProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


router.register(r'lists',CategoryViewSet,basename='lists')
router.register(r'tasks',OnlineProductViewSet,basename='tasks')


urlpatterns = router.urls