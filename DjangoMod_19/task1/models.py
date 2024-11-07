from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(decimal_places=2)
    size = models.DecimalField(decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name="games")

    def __str__(self):
        return self.title


"""

QuerySet запросы в порядке вызовов:

1.
Buyer.objects.create(name='Buyer 1', balance=100.00, age=25)
2.
Buyer.objects.create(name='Buyer 2', balance=200.00, age=17)
3.
Buyer.objects.create(name='Buyer 3', balance=300.00, age=30)
4.
Game.objects.create(title='Game 1', cost=50.00, size=1.5, description='Game 1 description', age_limited=False)
5.
Game.objects.create(title='Game 2', cost=75.00, size=2.0, description='Game 2 description', age_limited=True)
6.
Game.objects.create(title='Game 3', cost=100.00, size=3.0, description='Game 3 description', age_limited=False)
7.
game1.buyer.set([buyer1, buyer2, buyer3])
8.
game2.buyer.set([buyer1, buyer2])
9.
game3.buyer.set([buyer1, buyer3])
10.
Buyer.objects.filter(age__lt=18)
11.
Game.objects.filter(age_limited=True)
12.
games_with_age_limit.exclude(buyer=under_18_buyer).update(buyer=buyer1)


"""    