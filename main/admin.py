from django.contrib import admin

from main.models import *


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('player_id', 'old_club', 'new_club', 'price', 'price_tft','season_id', 'created_at' )
    list_filter = ('player_id', 'price', 'created_at' )

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','number', 'position', 'price', 'birth_date', 'club_id', 'country_id' )
    list_filter = ('club_id', 'country_id' )

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


