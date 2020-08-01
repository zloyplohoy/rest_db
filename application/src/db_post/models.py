from django.db import models


class PostData(models.Model):
    post_data = models.CharField(max_length=300, blank=True)
