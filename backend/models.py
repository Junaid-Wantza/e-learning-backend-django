from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model



class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50,default='',blank=True,null=True)
    last_name = models.CharField(max_length=50,default='',blank=True,null=True)
    avatar = models.ImageField(upload_to = 'uploads/avatars', default = 'no-img.jpg', blank=True,null=True)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(default='1975-12-12')
    bio = models.TextField(default='',blank=True,null=True)
    city = models.CharField(max_length=255, default='',blank=True,null=True)
    state = models.CharField(max_length=255, default='',blank=True,null=True)
    country = models.CharField(max_length=255, default='',blank=True,null=True)

    def __str__(self):
        return self.user.username



class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.content)


class Course(models.Model):
    title = models.CharField(max_length=200,default='',blank=True,null=True)
    description = models.TextField(default='Some default description')
    # cover_image = models.ImageField(upload_to='course_covers/')
    # enrollment_fee = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    # duration = models.PositiveIntegerField(help_text='Duration in days or weeks', null=True, blank=True)

    def __str__(self):
        return self.title


class LearningPath(models.Model):
    title = models.CharField(max_length=200,default='',blank=True,null=True)
    description = models.TextField(default='Some default description')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='learning_paths')

    def __str__(self):
        return self.title
    

class Module(models.Model):
    title = models.CharField(max_length=200,default='',blank=True,null=True)
    description = models.TextField(default='Some default description')
    learning_path = models.ForeignKey(LearningPath, on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.title
    

class Unit(models.Model):
    title = models.CharField(max_length=200,default='',blank=True,null=True)
    description = models.TextField(default='Some default description')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='units')

    def __str__(self):
        return self.title
    

class Content(models.Model):
    CONTENT_TYPES = (
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('quiz', 'Quiz'),
        # ('assignment', 'Assignment'),
        # Add more content types as needed
    )

    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField(default='Some default description')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_contents', null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='unit_contents', null=True, blank=True)

    def __str__(self):
        return self.title


class TextContent(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='text_contents',default='Module')
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title
    

class ImageContent(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='image_contents',default='Module')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='content_images/')

    def __str__(self):
        return self.title


class VideoContent(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='video_contents')
    title = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return self.title
    

class Quiz(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='quizzes',default='Module')
    title = models.CharField(max_length=200,default='Quiz')

    def __str__(self):
        return self.title
    

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()

    def __str__(self):
        return self.question_text\
        

class QuizChoice(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
    

class Assignment(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

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




class Answer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='answers')
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
