from rest_framework import routers
from universityApp.views.enrollment.enrollment_views import EnrollmentViewSet

router = routers.SimpleRouter()

router.register(r'enrollments', EnrollmentViewSet, basename="Enrollments")


urlpatterns = router.urls
