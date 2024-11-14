from django.db.models import (Model,
                              CharField,
                              DecimalField,
                              IntegerField,
                              TextField,
                              BooleanField,
                              ManyToManyField)

class Buyer(Model):
    name = CharField(max_length=100)
    balance = DecimalField(decimal_places=2, max_digits=5)
    age = IntegerField()

    def __str__(self):
        return self.name

class Game(Model):
    title = CharField(max_length=100)
    cost = DecimalField(decimal_places=2, max_digits=5)
    size = DecimalField(decimal_places=2, max_digits=5)
    description = TextField()
    age_limited = BooleanField()
    buyer = ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title






"""
python manage.py shell
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from task1.models import Game
>>> Game.objects.create(title='Game 4', cost=150.00, size=35, description='Game 4 description', age_limited=False)
<Game: Game 4>
>>> Game.objects.create(title='Game 5', cost=50.00, size=50, description='Game 5 description', age_limited=True)
<Game: Game 5>
>>> Game.objects.create(title='Game 6', cost=50.00, size=100, description='Game 6 description', age_limited=False)
<Game: Game 6>
>>> game = Game.objects.get(id=6)
>>> game.title = 'NEW Game 6'
>>> game.save()
>>> all_games = Game.objects.all()
>>> Game.objects.all()
<QuerySet [<Game: Game 1>, <Game: Game 2>, <Game: Game 3>, <Game: Game 4>, <Game: Game 5>, <Game: NEW Game 6>, <Game: Game 4>, <Game: Game 5>, <Game: Game 6>]>
>>> game_to_delete = Game.objects.get(id=7)
>>> game_to_delete.delete()
(1, {'task1.Game': 1})
>>> game_to_delete = Game.objects.get(id=8)
>>> game_to_delete.delete()
(1, {'task1.Game': 1})
>>>  game_to_delete = Game.objects.get(id=9)
  File "<console>", line 1
    game_to_delete = Game.objects.get(id=9)
IndentationError: unexpected indent
>>> Game.objects.all()
<QuerySet [<Game: Game 1>, <Game: Game 2>, <Game: Game 3>, <Game: Game 4>, <Game: Game 5>, <Game: NEW Game 6>, <Game: Game 6>]>
>>> Game.objects.filter(cost=50)
<QuerySet [<Game: Game 1>, <Game: Game 5>, <Game: NEW Game 6>, <Game: Game 6>]>
>>>
"""
