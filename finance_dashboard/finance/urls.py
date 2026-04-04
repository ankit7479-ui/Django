from rest_framework.routers import DefaultRouter
from .views import FinancialRecordViewSet

router = DefaultRouter()
router.register(r'records', FinancialRecordViewSet)

urlpatterns = router.urls