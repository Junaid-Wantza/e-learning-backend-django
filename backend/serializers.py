from rest_framework import serializers
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from .models import User, Profile, Announcement, Course, Tutorial, Notes, Quiz, Question, Answer, Student, Instructor, TakenQuiz, StudentAnswer
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_student', 'is_instructor', 'is_admin']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.password = make_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            validated_data['password'] = make_password(password)
        return super().update(instance, validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'avatar','phonenumber', 'birth_date', 'bio', 'city', 'state', 'country']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            profile = Profile.objects.create(user=user, **validated_data)
            return profile
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(instance=instance.user, data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        profile_serializer = super().update(instance, validated_data)
        return profile_serializer

class AnnouncementSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Announcement
        fields = ['id', 'user', 'content', 'posted_at' ]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'color']


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
        fields = ['id', 'owner', 'name', 'course' ]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text' ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'text', 'is_correct' ]


class InstructorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Instructor
        fields = ['id', 'user', 'interest' ]


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


class StudentAnswerSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    answer = AnswerSerializer()

    class Meta:
        model = StudentAnswer
        fields = ['id', 'user', 'quizzes', 'taken_quizzes' ]
