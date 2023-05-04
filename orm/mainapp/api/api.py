from django.http import JsonResponse
from django.views import View
from ..models import Stadium, Event, Team, Ticket


class StadiumsApi(View):
    def get(self, request):
        results: list = []
        data = Stadium.objects.all()
        for stadium in data:
            results.append({
                "id": stadium.id,
                "name": stadium.name,
                "location": stadium.location,
                "latitude": stadium.latitude,
                "longitude": stadium.longitude,
            })
        return JsonResponse({"stadiums": results})

class EventApi(View):
    def get(self, request):
        results: list = []
        data = Event.objects.all()
        for event in data:
            results.append({
                "stadium": {
                    "id": event.stadium.id,
                    "name": event.stadium.name,
                },
                "team_home": {
                    "country": event.team_home.country if event.team_home else None,
                    "cont": event.team_home.cont if event.team_home else None,
                },
                "team_away": {
                    "country": event.team_away.country if event.team_away else None,
                    "cont": event.team_away.cont if event.team_away else None,
                },
                "start": event.start,
            })
        return JsonResponse({"events": results})    
class EventOceaniaApi(View):
    def get(self, request):
        results: list = []
        data = Event.objects.filter(team_home__isnull=False, team_away__isnull=False,team_away__cont="Oceania")
        for eventOceania in data:
            results.append({
                "stadium": {
                    "id": eventOceania.stadium.id,
                    "name": eventOceania.stadium.name,
                },
                "team_home": {
                    "country": eventOceania.team_home.country if eventOceania.team_home else None,
                    "cont": eventOceania.team_home.cont if eventOceania.team_home else None,
                },
                "team_away": {
                    "country": eventOceania.team_away.country if eventOceania.team_away else None,
                    "cont": eventOceania.team_away.cont if eventOceania.team_away else None,
                },
                "start": eventOceania.start,
            })
        return JsonResponse({"eventsOceania": results})    

class TeamsApi(View):
    def get(self, request):
        results: list = []
        data = Team.objects.all()
        for team in data:
            results.append({
                "id": team.id,
                "country": team.country,
                "country_alpha2": team.country_alpha2,
                "nickname": team.nickname,
                "color_first": team.color_first,
                "color_second": team.color_second,
                "cont": team.cont,
            })
        return JsonResponse({"teams": results})

class TicketApi(View):
    def get(self, request, id):
        results: list = []
        ticket = Ticket.objects.get(id=id)
        results.append({
            "id": ticket.id,
            "category": ticket.category,
            "seat": ticket.seat,
            "price": ticket.price,
            "currency": ticket.currency,
            "event": {
                "id": ticket.event.id,
                "start": ticket.event.start,
                "stadium": {
                    "id": ticket.event.stadium.id,
                    "name": ticket.event.stadium.name,
                    "location": ticket.event.stadium.location,
                },
                "team_home": {
                    "country": ticket.event.team_home.country if ticket.event.team_home else None,
                },
                "team_away": {
                    "country": ticket.event.team_away.country if ticket.event.team_away else None,
                },
            },
        })
        return JsonResponse({"tickets": results})
