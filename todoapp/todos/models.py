from django.db import models

class Todo(models.Model):
    todo = models.CharField(max_length=100, null=False,
                            help_text="This field is required")
    done = models.BooleanField(default=False)
