from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .service import LeagueAPIClient

class SummonerByRiotIDView(APIView):
    def get(self, request, game_name, tag_line):
        client = LeagueAPIClient('br1')  # Ou a região desejada
        try:
            response = client.get_puuid_by_riot_id(game_name, tag_line)
            puuid = response['puuid']
            summoner = client.get_summoner_by_puuid(puuid)
            return Response(summoner, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
