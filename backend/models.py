from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model



class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to = 'uploads/avatars', default = 'no-img.jpg', blank=True)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(default='1975-12-12')
    bio = models.TextField(default='')
    city = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    country = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.user.username



class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.content)


class Course(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

class Tutorial(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    thumb = models.ImageField(upload_to='', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Notes(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to='', null=True, blank=True)
    cover = models.ImageField(upload_to='', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)    

  

class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz', related_name='students')
    interests = models.ManyToManyField(Course, related_name='interested_studentss')

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username



class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interest = models.ManyToManyField(Course, related_name="more_locations")


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_by')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)



class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers_submitted')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')    
