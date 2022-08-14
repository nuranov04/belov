from statistics import mode
from django.db import models

from core.models import BaseModel

class Video(BaseModel):
    title = models.CharField(max_length=256, default='no title')

    url = models.URLField(max_length=512)

    def __str__(self) -> str:
        return self.title
