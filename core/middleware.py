from django.core.cache import cache
from django.contrib import messages
from django.shortcuts import redirect
import time

class LoginAttemptMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/login/' and request.method == 'POST':
            ip = request.META.get('REMOTE_ADDR')
            attempts_key = f'login_attempts_{ip}'
            timeout_key = f'login_timeout_{ip}'
            
            # Check if user is in timeout
            if cache.get(timeout_key):
                messages.error(request, 'Too many failed attempts. Please try again later.')
                return redirect('login')
            
            # Track attempts
            attempts = cache.get(attempts_key, 0)
            if attempts >= 5:  # Max 5 attempts
                cache.set(timeout_key, True, 300)  # 5 minute timeout
                cache.delete(attempts_key)
                messages.error(request, 'Too many failed attempts. Please try again in 5 minutes.')
                return redirect('login')
            
            # Increment attempts counter
            cache.set(attempts_key, attempts + 1, 300)  # Reset after 5 minutes
            
        response = self.get_response(request)
        return response
