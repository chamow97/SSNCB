from django.db import models

class contests(models.Model):
    contest_name = models.CharField(max_length=300)
    date = models.DateField
    type = models.IntegerField
    start_time = models.DateTimeField
    end_time = models.DateTimeField
    is_rated = models.BooleanField(default=False)
    total_score = models.FloatField

class scoring(models.Model):
    user_id = models.IntegerField
    contest_id = models.IntegerField
    score_secured = models.FloatField
    total_score = models.FloatField

class user_details(models.Model):
    username = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    is_verified = models.BooleanField(default=False)
    profile_pic = models.FileField(null=True)
    number_of_contests = models.IntegerField(default=-1)
    
class questions(models.Model):
    contest_id = models.IntegerField
    question = models.CharField(max_length=2000)
    question_type = models.IntegerField

class answers(models.Model):
    question_id = models.IntegerField
    correct_option = models.IntegerField(default=-1)
    hint = models.CharField(max_length=2000)


    