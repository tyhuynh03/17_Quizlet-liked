from django.db import models
from users.models import User
from django.conf import settings
import uuid
from django.utils import timezone
class Topic(models.Model):
    name = models.CharField(max_length=255)
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.CharField(max_length=255)
    default_topic_id = 1  # ID của chủ đề mặc định đã tồn tại trong cơ sở dữ liệu
    image = models.ImageField(upload_to='question_images/', blank=True, null=True)  # Trường lưu trữ ảnh
    audio = models.FileField(upload_to='question_audios/', blank=True, null=True)   # Trường lưu trữ âm thanh
    topic = models.ForeignKey(Topic, related_name='questions', on_delete=models.CASCADE, default=default_topic_id)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class UserTopicScore(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)
    total_questions_answered = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.email} - {self.topic.name} - Correct: {self.correct_answers} - Incorrect: {self.incorrect_answers} - Total: {self.total_questions_answered}"