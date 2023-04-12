from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from .models import User, Profile, Announcement, Course, Tutorial, Notes, Quiz, Student, Instructor, TakenQuiz, Question, Answer
from .serializers import UserSerializer, ProfileSerializer, AnnouncementSerializer, CourseSerializer, TutorialSerializer, NotesSerializer, QuizSerializer, StudentSerializer, InstructorSerializer, TakenQuizSerializer, QuestionSerializer, AnswerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class AnnouncementViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

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

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class TakenQuizViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = TakenQuiz.objects.all()
    serializer_class = TakenQuizSerializer
