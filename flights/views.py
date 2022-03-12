from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger

def index(request):
       context = {
              "title": "Main Page",
              "flights":Flight.objects.all()
       }
       return render(request, 'flights/index.html', context)


def flight(request, flight_id):
       flight = Flight.objects.get(pk=flight_id)
       content = {
              "flight":flight,
              "passengers": flight.passengers.all(),
              "non_passengers": Passenger.objects.exclude(flights=flight).all(),
       }
       return render(request, "flights/flight.html", content)

def flights(request):
       content = {
              "flights": Flight.objects.all()
       }
       return render(request, "flights/flights.html", content)

def book(request, flight_id):
       if request.method == "POST":
              flight = Flight.objects.get(pk=flight_id)
              passenger = Passenger.objects.get(pk=request.POST["passenger"])
              passenger.flights.add(flight)
              return HttpResponseRedirect(reverse('flights:flight', args=[flight.id]))