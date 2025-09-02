from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse   # 👈 import HttpResponse to create a simple homepage

# Simple homepage view
def home(request):
    return HttpResponse("📚 Welcome to the Library Project Homepage!")

urlpatterns = [
    path('', home),                      # 👈 root URL (127.0.0.1:8000/)
    path('admin/', admin.site.urls),     # Django admin
    # path('books/', include('books.urls')),  # uncomment if you create a 'books' app
]
