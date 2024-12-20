from rest_framework.routers import DefaultRouter

from main.api_viewset import AccountViewSetsListAPIView

router = DefaultRouter()
router.register(r'', AccountViewSetsListAPIView)