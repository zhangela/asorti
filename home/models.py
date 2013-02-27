from django.db import models

class BetaSignup(models.Model):
    email = models.CharField(max_length=100)
    signed_up_on = models.DateTimeField()
