from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Course, Progress

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('course_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def track_progress(request, course_id):
    course = Course.objects.get(id=course_id)
    progress, created = Progress.objects.get_or_create(user=request.user, course=course)
    return render(request, 'track_progress.html', {'course': course, 'progress': progress})
