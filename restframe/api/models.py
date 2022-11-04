from django.db import models
from django.contrib.auth.models import User

class Leave(models.Model):
    LEAVE_TYPE = (
        ('C', 'Casual'),
        ('S', 'Sick'),
    )
    cause = models.CharField(max_length = 180)
    fromdt = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    status = models.BooleanField(default = False, blank = True)
    todate = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.cause