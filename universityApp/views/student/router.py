from rest_framework import routers
from universityApp.views.student.student_views import StudentViewSet, StudentsByCourse

router = routers.SimpleRouter()

router.register(r'students', StudentViewSet, basename="Students")
router.register(r'findByCourse', StudentsByCourse, basename="studentsByCourse")

urlpatterns = router.urls
