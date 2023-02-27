from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Games)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Genres)
admin.site.register(Player)
admin.site.register(Gender)
admin.site.register(Wallet)
admin.site.register(Sales)
admin.site.register(PayType)