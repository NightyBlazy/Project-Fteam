from rest_framework import serializers

from .models import Games, Developer, Publisher, Genres, Gender, Wallet, Player, Sales, PayType

class DeveloperSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Developer
        fields = '__all__'
        
class PublisherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = '__all__'

class GenresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genres
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    game_dev = serializers.SlugRelatedField(many=True, slug_field='developer_name', queryset=Developer.objects.all())
    game_pub = serializers.SlugRelatedField(many=True, slug_field='publisher_name', queryset=Publisher.objects.all())
    game_glist = serializers.SlugRelatedField(many=True, slug_field='genre_name', queryset=Genres.objects.all())
       
    class Meta:
        model = Games
        fields = ['game_id',
                  'game_name',
                  'game_dev',
                  'game_pub',
                  'game_glist',
                  'game_rating',
                  'game_desc',
                  'game_rdate',
                  'game_cover',
                  'game_price']
        
class GenderSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Gender
        fields = '__all__'
       
class WalletSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Wallet
        fields = ['wallet_id', 'wallet_owner', 'wallet_amount']
       
class PlayerSerializer(serializers.ModelSerializer):
    player_gender = serializers.SlugRelatedField(many=False, slug_field="gender_name", queryset=Gender.objects.all())
    player_owngames = serializers.SlugRelatedField(many=True, slug_field="game_name", queryset=Games.objects.all())
    player_wallet = serializers.SlugRelatedField(many=False, slug_field="wallet_amount", read_only=True)

    class Meta: 
        model = Player
        fields = ['player_id',
                  'player_name',
                  'player_gender',
                  'player_jdate',
                  'player_bdate',
                  'player_owngames',
                  'player_wallet']
 
class PayTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PayType
        fields = '__all__'
       
class SalesSerializer(serializers.ModelSerializer):
    sale_user = serializers.SlugRelatedField(many=False, slug_field="player_name", queryset=Player.objects.all())
    sale_soldgames = serializers.SlugRelatedField(many=True, slug_field="game_name",queryset=Games.objects.all())
    sale_paytype = serializers.SlugRelatedField(many=False, slug_field="paytype_name", queryset=PayType.objects.all())

    class Meta: 
        model = Sales
        fields = ['sale_id',
                  'sale_user',
                  'sale_soldgames',
                  'sale_date',
                  'sale_paytype',
                  'sale_price']
        
