from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("books/",list_books, name="book_list"),  # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
]
