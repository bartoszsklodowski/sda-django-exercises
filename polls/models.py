from django.db import models

# Create your models here.

class Poll(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Questions(models.Model):
    questions_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True, blank=True, related_name="questions")

    def __str__(self):
        return self.questions_text

class Answer(models.Model):
    answer_text = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True, blank=True, related_name="answers")

    def __str__(self):
        return self.answer_text