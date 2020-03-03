from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    username = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    desc = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    #StoreEvent.objects.all().order_by('-date')

    def __str__(self):
        return self.desc