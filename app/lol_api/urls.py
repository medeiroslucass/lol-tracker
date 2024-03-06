from django.urls import path
from .views import SummonerByRiotIDView

urlpatterns = [
    path('aaaaa', SummonerByRiotIDView.as_view(), name="summoner-list-view")
]