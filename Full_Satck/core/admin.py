from django.contrib import admin
from .models import UserProfile, DeepfakeDetectionLog, FraudDetectionLog

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'otp_enabled', 'created_at')
    search_fields = ('user__username', 'phone_number')

@admin.register(DeepfakeDetectionLog)
class DeepfakeDetectionLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_fake', 'confidence_score', 'created_at')
    list_filter = ('is_fake', 'created_at')
    search_fields = ('user__username',)

@admin.register(FraudDetectionLog)
class FraudDetectionLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_fraudulent', 'risk_score', 'created_at')
    list_filter = ('is_fraudulent', 'created_at')
    search_fields = ('user__username',)
