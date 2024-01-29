from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import Participant
from event_management.models import Event

def register_participant(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        event = request.POST.get('event')  # Assuming 'event' is the name of the field for event selection in the form

        # Create a new participant instance and save it
        event = Event.objects.get(pk=event)
        participant = Participant(name=name, surname=surname, email=email, event=event)
        participant.save()

        # Build the accept URL manually
        accept_url = request.build_absolute_uri(f'/participants/accept/{participant.id}/')
        decline_url = request.build_absolute_uri(f'/participants/decline/{participant.id}/')

        # Send an email to the participant
        subject = 'Invitation Confirmation'
        message = f'Hello {participant.name},\n\nYou have been invited to the event.\n\nAccept: {accept_url}\nDecline: {decline_url}'
        sender_email = 'praktnicnitest@gmail.com'

        send_mail(subject, message, sender_email, [participant.email])

        return redirect('home')
    
    events = Event.objects.all()
    return render(request, 'participant_management/register_participant.html', {'events': events})

def accept(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    participant.accepted = True
    participant.save()
    return render(request, 'participant_management/invitation_accepted.html')

def decline(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    participant.delete()
    return render(request, 'participant_management/invitation_declined.html')
