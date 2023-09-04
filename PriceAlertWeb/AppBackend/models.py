from django.db import models
class UserDetail(models.Model):
    name = models.TextField(max_length=60)
    interest = models.CharField(max_length=60)
    def __str__(self):
        return self.name

