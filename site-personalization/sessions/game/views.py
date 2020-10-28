from django.shortcuts import render
from .models import Player, Game, PlayerGameInfo
import random


def show_home(request):
    if 'player_id' not in request.session:
        player = Player.objects.create()
        request.session['player_id'] = player.id
    if ('game_id' not in request.session) or (Game.objects.get(id=request.session['game_id']).its_over == True):
        if Game.objects.all().filter(its_over=False):
            game = Game.objects.all().filter(its_over=False)[0]
            request.session['game_id'] = game.id
            player = Player.objects.get(id=request.session['player_id'])
            player.name = "player"
            player.save()
            info = PlayerGameInfo.objects.create(player=player, game=game, counter=0, starter=False)
        else:
            number = random.randint(0, 10)
            game = Game.objects.create(number=number, its_over=False)
            request.session['game_id'] = game.id
            player = Player.objects.get(id=request.session['player_id'])
            player.name = "starter"
            player.save()
            info = PlayerGameInfo.objects.create(player=player, game=game, counter=0, starter=True)
    game_id = request.session['game_id']
    player_id = request.session['player_id']
    info = PlayerGameInfo.objects.get(player_id=player_id, game_id=game_id)
    if info.starter:
        counter = 0
        for i in PlayerGameInfo.objects.all().filter(game_id=game_id):
            counter += i.counter
        return render(request,'home.html',{'info': info,'counter': counter})
    else:
        num = request.POST.get('number', default=None)
        info.counter += 1
        info.save()
        if num == None:
            num = 0
        num = int(num)
        if num < info.game.number:
            hint = f'Загаданое число больше {num}'
        elif num > info.game.number:
            hint = f'Загаданое число меньше {num}'
        else:
            hint = 'Вы угадали число'
            info.game.its_over = True
            info.game.save()
        return render(
            request,
            'home.html',
            {'info': info,
            'hint': hint}
            )
