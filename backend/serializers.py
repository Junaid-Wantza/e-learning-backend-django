from rest_framework import serializers
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from .models import User, Profile, Announcement, Course, LearningPath, Module, Unit, Content, TextContent, ImageContent, VideoContent, QuizChoice, QuizQuestion, Assignment, Tutorial, Notes, Quiz, Answer, Student, Instructor, TakenQuiz, StudentAnswer
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenObtainPairSerializerWithUsername(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
    

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Customize the token payload if needed
        # For example, you can add extra user-related data to the token

        return token



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'is_student', 'is_instructor', 'is_admin']
        extra_kwargs = {
            'username': {'validators': []},  # Remove uniqueness validator for username in the update
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        return super().update(instance, validated_data)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'avatar','phonenumber', 'birth_date', 'bio', 'city', 'state', 'country']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            profile = Profile.objects.create(user=user, **validated_data)
            return profile
        else:
            raise serializers.ValidationError(user_serializer.errors)

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user_instance = instance.user  # Get the existing user instance

        # Update the user fields with the provided data
        user_serializer = UserSerializer(instance=user_instance, data=user_data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        profile = super().update(instance, validated_data)
        return profile

class AnnouncementSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Announcement
        fields = ['id', 'user', 'content', 'posted_at' ]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description']


class LearningPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningPath
        fields = ['id', 'title', 'description', 'course']


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'title', 'description', 'learning_path']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'title', 'description', 'module']


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'content_type', 'title', 'description', 'course', 'unit']


class TextContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent
        fields = ['id', 'module', 'title', 'text']

class ImageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageContent
        fields = ['id', 'module', 'title', 'image']

class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = ['id', 'module', 'title', 'video_url']


class TutorialSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseSerializer()

    class Meta:
        model = Tutorial
        fields = ['id', 'title', 'content', 'thumb', 'course', 'created_at', 'user' ]


class NotesSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseSerializer()

    class Meta:
        model = Notes
        fields = ['id', 'title', 'file', 'cover', 'course', 'user' ]


class QuizSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'module' ]


class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['question_text']

class QuizChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizChoice
        fields = ['choice_text', 'is_correct']


class InstructorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Instructor
        fields = ['user', 'interest' ]


class TakenQuizSerializer(serializers.ModelSerializer):
    quiz = serializers.StringRelatedField()

    class Meta:
        model = TakenQuiz
        fields = ['student', 'quiz', 'score', 'date']


class StudentSerializer(serializers.ModelSerializer):
    taken_quizzes = TakenQuizSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['user', 'quizzes', 'taken_quizzes']
