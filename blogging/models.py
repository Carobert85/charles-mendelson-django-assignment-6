from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField(blank=True)  # blog text is too long for a CharField
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # should reference a primary key on the user table
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
