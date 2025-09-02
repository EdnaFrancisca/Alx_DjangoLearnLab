from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Simple homepage view
def home(request):
    return HttpResponse("<h1>Welcome to the Library Project</h1>")

urlpatterns = [
    path('', home),           # Root URL (http://127.0.0.1:8000/)
    path('admin/', admin.site.urls),
]
