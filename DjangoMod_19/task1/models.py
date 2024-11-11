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



# """
# QuerySet запросы в порядке вызовов:
#
# 1.
# Buyer.objects.create(name='Buyer 1', balance=100.00, age=25)
# 2.
# Buyer.objects.create(name='Buyer 2', balance=200.00, age=17)
# 3.
# Buyer.objects.create(name='Buyer 3', balance=300.00, age=30)
# 4.
# Game.objects.create(title='Game 1', cost=50.00, size=1.5, description='Game 1 description', age_limited=False)
# 5.
# Game.objects.create(title='Game 2', cost=75.00, size=2.0, description='Game 2 description', age_limited=True)
# 6.
# Game.objects.create(title='Game 3', cost=100.00, size=3.0, description='Game 3 description', age_limited=False)
# 7.
# game1.buyer.set([buyer1, buyer2, buyer3])
# 8.
# game2.buyer.set([buyer1, buyer2])
# 9.
# game3.buyer.set([buyer1, buyer3])
# 10.
# Buyer.objects.filter(age__lt=18)
# 11.
# Game.objects.filter(age_limited=True)
# 12.
# games_with_age_limit.exclude(buyer=under_18_buyer).update(buyer=buyer1)
#
#
# """
#
# """
#
# """


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