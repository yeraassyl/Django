from mid.api.views import BookListViewSet, JournalListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'books', BookListViewSet)
router.register(r'journals', JournalListViewSet)

urlpatterns = router.urls