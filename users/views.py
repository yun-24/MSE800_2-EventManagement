from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from events.models import Event

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('events:event_list')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('events:event_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('events:event_list')


def personal_center(request):
    if request.user.is_authenticated:
        user_events = Event.objects.filter(organizer=request.user)
        attending_events = Event.objects.filter(attendees=request.user)
        return render(request, 'users/personal_center.html',
                      {'username': request.user.username,
                       'user_events': user_events,
                       'attending_events': attending_events
                       })
    else:
        # Handle the case where the user is not logged in
        return redirect('events:event_list')