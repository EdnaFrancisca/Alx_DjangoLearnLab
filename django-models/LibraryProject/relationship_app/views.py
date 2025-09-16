from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic import DetailView
from .models import Library,Book


# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatically log in new user
            return redirect("home")  # make sure you have a "home" URL configured
    else:
        form = UserCreationForm()

    # ✅ explicitly referencing relationship_app/register.html
    return render(request, "relationship_app/register.html", {"form": form})


def list_books(request):
    books = Book.objects.all()  
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
