from rest_framework import routers
from universityApp.views.course.course_views import CourseViewSet, CoursesBySemester, CoursesByStudent

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet)
router.register(r'my-courses', CoursesByStudent, basename="my-courses")
router.register(r'findBySemester', CoursesBySemester, basename='coursesBySemester')
urlpatterns = router.urls
