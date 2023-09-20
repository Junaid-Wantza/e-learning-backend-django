from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Profile, Announcement, Course, LearningPath, Module, Unit, Content, TextContent, ImageContent, VideoContent, Tutorial, Notes, Quiz, QuizChoice, QuizQuestion, Student, Instructor, TakenQuiz, Answer
from .serializers import LoginSerializer,UserSerializer, ProfileSerializer, AnnouncementSerializer, CourseSerializer, LearningPathSerializer, ModuleSerializer, UnitSerializer, ContentSerializer, TextContentSerializer, VideoContentSerializer, ImageContentSerializer, TutorialSerializer, NotesSerializer, QuizSerializer, QuizQuestionSerializer, QuizChoiceSerializer, StudentSerializer, InstructorSerializer, TakenQuizSerializer, TokenObtainPairSerializerWithUsername
from rest_framework_simplejwt.views import TokenObtainPairView

class TokenObtainPairWithUsernameView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializerWithUsername


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def get_by_username(self, request):
        username = request.query_params.get('username')
        if username:
            try:
                user = User.objects.get(username=username)
                serializer = self.get_serializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response({'detail': 'User not found.'}, status=404)
        else:
            return Response({'detail': 'Username parameter is missing.'}, status=400)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminUser]
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



class AnnouncementViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [IsAuthenticated]


class LearningPathViewSet(viewsets.ModelViewSet):
    queryset = LearningPath.objects.all()
    serializer_class = LearningPathSerializer
    # permission_classes = [IsAuthenticated]

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    # permission_classes = [IsAuthenticated]

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    # permission_classes = [IsAuthenticated]

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    # permission_classes = [IsAuthenticated]

class TextContentViewSet(viewsets.ModelViewSet):
    queryset = TextContent.objects.all()
    serializer_class = TextContentSerializer
    # permission_classes = [IsAuthenticated]

class ImageContentViewSet(viewsets.ModelViewSet):
    queryset = ImageContent.objects.all()
    serializer_class = ImageContentSerializer
    # permission_classes = [IsAuthenticated]

class VideoContentViewSet(viewsets.ModelViewSet):
    queryset = VideoContent.objects.all()
    serializer_class = VideoContentSerializer
    # permission_classes = [IsAuthenticated]


class TutorialViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

class NotesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

class QuizViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizQuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer

class QuizChoiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = QuizChoice.objects.all()
    serializer_class = QuizChoiceSerializer

class StudentViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class TakenQuizViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = TakenQuiz.objects.all()
    serializer_class = TakenQuizSerializer
