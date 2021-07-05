from django.db import models


class Languages(models.Model):
    name = models.CharField(max_length=50)
    added_at = models.DateTimeField(auto_now_add=True)
