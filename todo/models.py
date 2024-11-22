from django.db import models

class TodoModel(models.Model):
    text = models.CharField(max_length=255, default="")
    time = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    is_urgent = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text