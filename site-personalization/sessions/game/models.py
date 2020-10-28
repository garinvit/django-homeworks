from django.db import models


class Player(models.Model):
    name = models.TextField()


class Game(models.Model):
    game_info = models.ManyToManyField(Player, through='PlayerGameInfo')
    number = models.IntegerField()
    its_over = models.BooleanField(default=False)

class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    counter = models.IntegerField()
    starter = models.BooleanField()