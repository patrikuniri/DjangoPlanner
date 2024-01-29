from django.shortcuts import render, redirect
from .models import Event
from participant_management.models import Participant
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    events = Event.objects.all()
    participants = Participant.objects.all()
    accepted_participants = Participant.objects.filter(accepted=True)
    return render(request, 'event_management/home.html', {'events': events, "participants": participants, 'accepted_participants': accepted_participants})

def create_event(request):
    if request.method == 'POST':
        name = request.POST.get('event_name')
        place = request.POST.get('event_place')
        date = request.POST.get('event_date')
        time = request.POST.get('event_time')
        event = Event.objects.create(name=name, place=place, date=date, time=time)
        return redirect('home')

def manage_participants(request):
    participants = Participant.objects.all()
    return render(request, 'participant_management/manage_participants.html', {'participants': participants})

def delete_event(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, pk=event_id)
        event.delete()
        return redirect('home')

def delete_participant(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    if request.method == 'POST':
        participant.delete()
        return redirect('home')
    return render(request, 'event_management/home.html', {'participant': participant})

