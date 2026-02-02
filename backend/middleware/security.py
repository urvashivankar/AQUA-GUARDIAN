
from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from collections import defaultdict
from datetime import datetime, timedelta
import time
import re

# Rate limiting storage (in production, use Redis)
request_counts = defaultdict(lambda: {"count": 0, "reset_time": datetime.now()})

class SecurityMiddleware(BaseHTTPMiddleware):    
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        
        return response

class RateLimitMiddleware(BaseHTTPMiddleware):
    
    def __init__(self, app, requests_per_minute: int = 60):
        super().__init__(app)
        self.requests_per_minute = requests_per_minute
        self.window_seconds = 60
    
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        
        if request.url.path in ["/", "/health", "/docs", "/openapi.json"]:
            return await call_next(request)
        
        current_time = datetime.now()
        client_data = request_counts[client_ip]
        
        if current_time >= client_data["reset_time"]:
            client_data["count"] = 0
            client_data["reset_time"] = current_time + timedelta(seconds=self.window_seconds)
        
        client_data["count"] += 1
        
        if client_data["count"] > self.requests_per_minute:
            retry_after = int((client_data["reset_time"] - current_time).total_seconds())
            return JSONResponse(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                content={
                    "error": "Rate limit exceeded",
                    "message": f"Too many requests. Please try again in {retry_after} seconds.",
                    "retry_after": retry_after
                },
                headers={"Retry-After": str(retry_after)}
            )
        
        response = await call_next(request)
        response.headers["X-RateLimit-Limit"] = str(self.requests_per_minute)
        response.headers["X-RateLimit-Remaining"] = str(self.requests_per_minute - client_data["count"])
        response.headers["X-RateLimit-Reset"] = str(int(client_data["reset_time"].timestamp()))
        
        return response

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_coordinates(latitude: float, longitude: float) -> bool:
    return -90 <= latitude <= 90 and -180 <= longitude <= 180

def sanitize_input(text: str, max_length: int = 1000) -> str:
    if not text:
        return ""
    
    sanitized = text.strip()
    
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    
    sanitized = re.sub(r'<[^>]+>', '', sanitized)
    
    dangerous_patterns = [
        r'(\bDROP\b|\bDELETE\b|\bINSERT\b|\bUPDATE\b)',
        r'(--|;|\/\*|\*\/)',
        r'(\bOR\b.*=.*\bOR\b)',
        r'(\bAND\b.*=.*\bAND\b)'
    ]
    
    for pattern in dangerous_patterns:
        sanitized = re.sub(pattern, '', sanitized, flags=re.IGNORECASE)
    
    return sanitized

def validate_severity(severity: int) -> bool:
    return 1 <= severity <= 5

def validate_file_upload(filename: str, max_size_mb: int = 10) -> tuple[bool, str]:
    allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
    file_ext = '.' + filename.lower().split('.')[-1] if '.' in filename else ''
    
    if file_ext not in allowed_extensions:
        return False, f"Invalid file type. Allowed: {', '.join(allowed_extensions)}"
    
    if re.search(r'[<>:"/\\|?*]', filename):
        return False, "Filename contains invalid characters"
    
    return True, "Valid"

class InputValidationError(Exception):
    pass
