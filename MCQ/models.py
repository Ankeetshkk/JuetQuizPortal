from django.db import models

class Qcontent(models.Model):
    content=models.CharField(max_length=512)


class Qoptions(models.Model):
    options1=models.CharField(max_length=51)
    options2=models.CharField(max_length=51)
    options3=models.CharField(max_length=51)
    options4=models.CharField(max_length=51) 

class CorrectAnswer(models.Model):
    correctAnswer=models.CharField(max_length=51)
    
class AnswerSubmitted(models.Model):
    answerSubmitted=models.CharField(max_length=51)

class Meta:
    db_table = "MCQ"
# Create your models here.
