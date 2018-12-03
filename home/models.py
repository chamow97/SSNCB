from datetime import date
from django.db import models
from django.utils.timezone import now

class contests(models.Model):

    contest_types = (
        ('MCQ', 'MCQ'),
        ('Coding', 'Coding')
    )
    contest_name = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True, null=True)
    type = models.CharField(max_length=100, choices=contest_types)
    start_time = models.DateTimeField(auto_now_add=True, null=True)
    end_time = models.DateTimeField(auto_now_add=True, null=True)
    is_rated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " " + str(self.contest_name)

class scoring(models.Model):
    user_id = models.IntegerField(default=-1)
    contest_id = models.IntegerField(default=-1)
    score_secured = models.FloatField(default=-1.0)
    total_score = models.FloatField(default=-1.0)

class user_details(models.Model):
    username = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    is_verified = models.BooleanField(default=False)
    profile_pic = models.FileField(null=True)
    number_of_contests = models.IntegerField(default=-1)
    
class questions(models.Model):
    contest_id = models.IntegerField(default=-1)
    question = models.CharField(max_length=2000)
    description = models.CharField(max_length=20000, default='NA')
    constraints = models.CharField(max_length=2000, default='NA')
    sample_testcases = models.CharField(max_length=20000, default='NA')
    editorial = models.CharField(max_length=40000, default='WA')
    is_solved = models.BooleanField(default=False)
    score_secured = models.IntegerField(default=0)

    def __str__(self):
        return "Contest " + \
               str(self.contest_id) + \
               ", Id: " + str(self.id) + \
               ", Question: " + \
               str(self.question)

class answers(models.Model):
    question_id = models.IntegerField(default=-1)
    correct_option = models.CharField(default='NA', max_length=2000)

class tests(models.Model):
    input_file = models.FileField(null=True)
    output_file = models.FileField(null=True)

class choices(models.Model):
    question_id = models.IntegerField(default=-1)
    choice = models.CharField(default='NA', max_length=2000)

    def __str__(self):
        return "Q Id: " + str(self.question_id) +\
               ", Choice: " + str(self.choice)

class editor_themes(models.Model):
    theme_name = models.CharField(max_length=100)
    theme_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.theme_name)

class editor_language(models.Model):
    language_name = models.CharField(max_length=100)
    language_id = models.CharField(max_length=100)
    sample_code = models.TextField(max_length=100000)

    def __str__(self):
        return str(self.language_name)

    