from django.urls import path
# Import des URLs de l'interface d'administration
from django.contrib import admin
# Import des vues qui sont déclarées dans leur propre module (dossier)
from .views import HomeView, StadiumsView, TeamsView, NewsletterView, UpdateView, AboutView
from .api import EventApi, StadiumsApi, TeamsApi, TicketApi, EventOceaniaApi

urlpatterns = (
    path("", HomeView.as_view(), name="home"),
    path("stadiums", StadiumsView.as_view(), name="stadiums"),
    path("teams", TeamsView.as_view(), name="teams"),
    path("newsletter", NewsletterView.as_view(), name="newsletter"),
    path("update", UpdateView.as_view(), name="update"),
    # Dans un cadre de projet réel, il serait préférable d'utiliser une URL moins prévisible que "admin"
    path("admin", admin.site.urls),
    path("about", AboutView.as_view(), name="about"),
    path("api/stadiums", StadiumsApi.as_view()),
    path("api/events", EventApi.as_view()),
    path("api/teams", TeamsApi.as_view()),
    path("api/ticket/<str:id>", TicketApi.as_view()),
    path("api/eventsOceania", EventOceaniaApi.as_view()),

)
