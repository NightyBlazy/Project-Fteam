from .models import Games, Player, Developer, Publisher, Genres, Sales, Wallet, PayType
from .serializers import GameSerializer, PlayerSerializer, DeveloperSerializer, PublisherSerializer, GenresSerializer, SalesSerializer, WalletSerializer, PayTypeSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

# Create your views here.

class GamesViewSet(ModelViewSet):
    queryset = Games.objects.all()
    
    serializer_class = GameSerializer
    
    parser_classes = (MultiPartParser,FormParser)
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    
class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    
    serializer_class = PlayerSerializer
    
    parser_classes = (MultiPartParser,FormParser)
     
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    
    
    def perform_create(self, serializer):
        new_wallet = Wallet.objects.create(wallet_owner= serializer.validated_data['player_name'])
        return serializer.save(player_wallet = new_wallet)
    

class DevelopersViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    
    serializer_class = DeveloperSerializer
    
    parser_classes = (MultiPartParser,FormParser)
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

class PublishersViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    
    serializer_class = PublisherSerializer
    
    parser_classes = (MultiPartParser,FormParser)
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

class GenresViewSet(ModelViewSet):
    queryset = Genres.objects.all()
    
    serializer_class = GenresSerializer
    
    parser_classes = (MultiPartParser,FormParser)
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    
class SalesViewSet(ModelViewSet):
    queryset = Sales.objects.all()
    
    serializer_class = SalesSerializer
    
    parser_classes = (MultiPartParser,FormParser)
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    


@api_view(['PATCH'])
def add_money(request,pk=None):
    addamount = JSONParser().parse(request) 
    data = Player.objects.get(player_id = pk)
    wallet = Wallet.objects.get(wallet_id = data.player_wallet.wallet_id)
    
    current_amount = {'wallet_amount':wallet.wallet_amount + addamount['amount']}
    
    print(current_amount)
    
    walletserializer = WalletSerializer(wallet, data=current_amount, partial=True)
    
    if walletserializer.is_valid(raise_exception=True):    
        walletserializer.save()
        playerserializer = PlayerSerializer(data)
        return Response(playerserializer.data['player_wallet'])

    return Response({'error': "Error occured!"})
    

@api_view(['PATCH'])
def spend_money(request,pk=None):
    addamount = JSONParser().parse(request) 
    data = Player.objects.get(player_id = pk)
    wallet = Wallet.objects.get(wallet_id = data.player_wallet.wallet_id)
    
    current_amount = {'wallet_amount':wallet.wallet_amount - addamount['amount']}
    
    print(current_amount)
    
    walletserializer = WalletSerializer(wallet, data=current_amount, partial=True)
    
    if walletserializer.is_valid(raise_exception=True):    
        walletserializer.save()

    playerserializer = PlayerSerializer(data)
    return Response(playerserializer.data['player_wallet'])