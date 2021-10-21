from django.db import models
from django.contrib.auth.models import User # connect each post to a user!

class Post(models.Model):
    # title, date, timespent, what I learned
    title = models.CharField(max_length=100)
    date = models.DateField()
    timespent = models.CharField(max_length=100)
    what_i_learned = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # connect each post to a user!

    def __str__(self):
        return self.title 

    def get_title(self):
        title = self.title 
        return title 

    def get_date(self):
        date = str(self.date)
        return date 

