from rest_framework import routers
from universityApp.views.course.course_views import CourseViewSet, CoursesByStudent

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet)
router.register(r'my-courses', CoursesByStudent, basename="my-courses")
urlpatterns = router.urls
