from rest_framework import routers
from universityApp.views.student.student_views import GetMyInfo, StudentViewSet, StudentsByCourse

router = routers.SimpleRouter()

router.register(r'students', StudentViewSet, basename="Students")
router.register(r'findByCourse', StudentsByCourse, basename="studentsByCourse")
router.register(r'getMyInfo', GetMyInfo, basename="getMyInfo")

urlpatterns = router.urls
