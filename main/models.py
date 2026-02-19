from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Season(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='club/', blank=True)
    president = models.CharField(max_length=100, blank=True, null=True )
    coach = models.CharField(max_length=100, blank=True, null=True )
    found_date = models.DateField(blank=True, null=True)

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)],
        blank=True, null=True
    )
    position = models.CharField(blank=True, null=True, max_length=100)
    price = models.FloatField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    club_id = models.ForeignKey(Club, on_delete=models.SET_NULL, blank=True, null=True)
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Transfer(models.Model):
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True)
    old_club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True, related_name='import_transfer')
    new_club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True, related_name='export_transfer')
    price = models.FloatField(blank=True, null=True)
    price_tft = models.FloatField(blank=True, null=True)

    season_id = models.ForeignKey(Season, on_delete=models.SET_NULL, blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
