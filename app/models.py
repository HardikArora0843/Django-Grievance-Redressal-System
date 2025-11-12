from django.contrib.auth.models import AbstractUser
from django.db import models

PRIORITY_CHOICES = (
    ("Normal", "Normal"),
    ("Medium", "Medium"),
    ("High", "High"),
)

STATUS_CHOICES = (
    ("Registered", "Registered"),
    ("Under Review", "Under Review"),
    ("Closed", "Closed")
)

class User(AbstractUser):
    phone_number = models.BigIntegerField(default=0)  # ✅ changed to BigIntegerField
    address = models.CharField(max_length=500, default="No Value")
    state = models.CharField(max_length=100, default="No Value")
    gender = models.CharField(max_length=50, default="No Value")
    handler = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}, Handler: {self.handler}"


class Grievance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    category = models.CharField(max_length=100)
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default="Normal")
    details = models.CharField(max_length=2000)
    about = models.CharField(max_length=500, default="No Value")
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="Registered")
    created_at = models.DateTimeField(auto_now_add=True)
    ref_no = models.BigIntegerField(default=100)  # ✅ changed to BigIntegerField
    handler_response = models.CharField(max_length=500, default="")
    satisfied = models.BooleanField(default=False)

    def __str__(self):
        return f"Grievance: {self.id} Time: {self.created_at}"


class Escalate(models.Model):
    ref_no = models.BigIntegerField(default=100)  # ✅ changed to BigIntegerField
    reason = models.CharField(max_length=500)
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default="Normal")

    def __str__(self):
        return f"G: {self.ref_no} P increased to {self.priority}"
