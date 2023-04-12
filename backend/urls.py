from rest_framework import routers
from .views import UserViewSet, ProfileViewSet, AnnouncementViewSet, CourseViewSet, TutorialViewSet, NotesViewSet, QuizViewSet, StudentViewSet, InstructorViewSet, TakenQuizViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'tutorials', TutorialViewSet)
router.register(r'notes', NotesViewSet)
router.register(r'quiz', QuizViewSet)
router.register(r'students', StudentViewSet)
router.register(r'instructors', InstructorViewSet)
router.register(r'taken_quiz', TakenQuizViewSet)

urlpatterns = router.urls
