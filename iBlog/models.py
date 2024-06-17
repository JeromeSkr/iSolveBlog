from django.db import models
from django.contrib.auth.models import User

class IBlogModel(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return self.title