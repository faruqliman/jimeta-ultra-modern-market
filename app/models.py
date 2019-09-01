from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
	v_type = models.CharField(max_length=50)
	amount = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)
	gate = models.CharField(max_length=20)
	user = models.ForeignKey(User, on_delete=models.CASCADE)