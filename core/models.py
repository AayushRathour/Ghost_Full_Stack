from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    otp_enabled = models.BooleanField(default=False)
    voice_print = models.FileField(upload_to='voice_prints/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class DeepfakeDetectionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='deepfake_checks/')
    is_fake = models.BooleanField()
    confidence_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {'Fake' if self.is_fake else 'Real'} - {self.created_at}"

class FraudDetectionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_data = models.JSONField()
    is_fraudulent = models.BooleanField()
    risk_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {'Fraudulent' if self.is_fraudulent else 'Legitimate'} - {self.created_at}"
