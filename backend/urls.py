from rest_framework import routers
from django.urls import path, include
from .views import TokenObtainPairWithUsernameView
from .views import LoginView, UserViewSet, ProfileViewSet, AnnouncementViewSet, CourseViewSet, LearningPathViewSet, ModuleViewSet, UnitViewSet, ContentViewSet, TextContentViewSet, ImageContentViewSet, VideoContentViewSet, TutorialViewSet, NotesViewSet, QuizViewSet, QuizQuestionViewSet, QuizChoiceViewSet, StudentViewSet, InstructorViewSet, TakenQuizViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'learningpaths', LearningPathViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'units', UnitViewSet)
router.register(r'content', ContentViewSet)
router.register(r'textcontent', TextContentViewSet)
router.register(r'imagecontent', ImageContentViewSet)
router.register(r'videocontent', VideoContentViewSet)
router.register(r'tutorials', TutorialViewSet)
router.register(r'notes', NotesViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuizQuestionViewSet)
router.register(r'quizchoice', QuizChoiceViewSet)
router.register(r'students', StudentViewSet)
router.register(r'instructors', InstructorViewSet)
router.register(r'taken_quiz', TakenQuizViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('api/token/', TokenObtainPairWithUsernameView.as_view(), name='token_obtain_pair'),
    path("", include(router.urls))
]