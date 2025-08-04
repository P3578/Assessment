from django.db import models

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    language = models.CharField(max_length=100,default='python')
    linenos = models.BooleanField(default=False)
    style = models.CharField(max_length=100,default='friendly')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)