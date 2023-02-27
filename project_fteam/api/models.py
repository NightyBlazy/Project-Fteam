from django.db import models
from PIL import Image
import uuid
from annoying.fields import AutoOneToOneField

# Create your models here.

class Genres(models.Model):
    genre_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    genre_name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.genre_name
    
class Developer(models.Model):
    developer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    developer_name = models.CharField(max_length=50, blank=False)
    developer_fdate = models.CharField(max_length=10,blank=False)
    developer_adress = models.TextField(blank=True, default="Blank adress")
    def __str__(self):
        return self.developer_name
    
class Publisher(models.Model):
    publisher_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    publisher_name = models.CharField(max_length=50, blank=False)
    publisher_fdate = models.CharField(max_length=10,blank=False)
    publisher_adress = models.TextField(blank=True, default="Blank adress")
    def __str__(self):
        return self.publisher_name

class Games(models.Model):
    game_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game_name = models.CharField(max_length=50, blank=False)
    game_dev = models.ManyToManyField(Developer, blank=False)
    game_pub = models.ManyToManyField(Publisher, blank=False)
    game_glist = models.ManyToManyField(Genres, blank=False)
    game_rating = models.IntegerField(blank=False)
    game_desc = models.TextField(blank=True, default="Blank Description")
    game_rdate = models.CharField(max_length=10,blank=False)
    game_cover = models.ImageField(upload_to='game_covers',default='default_cover.jpg')
    game_price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.game_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.game_cover.path)
        
        if img.height > 600 or img.width > 400:
            output_size = (400,600)
            img.thumbnail(output_size)
            img.save(self.game_cover.path)
        
class Gender(models.Model):
    gender_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gender_name = models.CharField(max_length=10, blank=False)
      
    def __str__(self):
        return self.gender_name
  
class Wallet(models.Model):
    wallet_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet_owner = models.CharField(max_length=50, blank=False)
    wallet_amount = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.wallet_owner}'s Wallet"
         
class Player(models.Model):
    player_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player_name = models.CharField(max_length=50, blank=False)
    player_gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=False)
    player_jdate = models.CharField(max_length=10,blank=False)
    player_bdate = models.CharField(max_length=10,blank=False)
    player_owngames = models.ManyToManyField(Games, blank=True)
    player_wallet = models.OneToOneField(Wallet, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.player_name
    
class PayType(models.Model):
    paytype_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paytype_name = models.CharField(max_length=10,blank=False)
    paytype_rate = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.paytype_name
    
class Sales(models.Model):
    sale_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale_user = models.ForeignKey(Player, on_delete=models.CASCADE, blank=False)
    sale_soldgames = models.ManyToManyField(Games, blank=False)
    sale_date = models.CharField(max_length=10,blank=False)
    sale_paytype = models.ForeignKey(PayType, on_delete=models.CASCADE)
    sale_price = models.DecimalField(max_digits=50, decimal_places=2)
    