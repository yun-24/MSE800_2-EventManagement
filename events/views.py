from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .forms import EventForm
from .models import Event


# Create your views here.


def event_list(request):
    events = Event.objects.all().order_by('date_time')
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    attendees = event.attendees.all()

    if request.method == 'POST':
        if request.POST.get('action') == 'attend':
            event.attendees.add(request.user)
        elif request.POST.get('action') == 'unattend':
            event.attendees.remove(request.user)
        return redirect('events:event_detail', pk=event.pk)

    return render(request, 'events/event_detail.html', {
        'event': event,
        'attendees': attendees,
    })


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('events:event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})


@login_required
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk, organizer=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form, 'event': event})


@login_required
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    # Check if the user is a staff member (admin)
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to delete events.')
        return redirect('events:event_detail', pk=event.pk)

    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully.')
        return redirect('events:event_list')

    # redirect back to event detail page
    return redirect('events:event_detail', pk=event.pk)
