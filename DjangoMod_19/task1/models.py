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
from django.db.models import Q

# Create 3 Buyer records
buyer1 = Buyer.objects.create(name='Buyer 1', balance=100.00, age=25)
buyer2 = Buyer.objects.create(name='Buyer 2', balance=200.00, age=17)
buyer3 = Buyer.objects.create(name='Buyer 3', balance=300.00, age=30)

# Create 3 Game records
game1 = Game.objects.create(title='Game 1', cost=50.00, size=1.5, description='Game 1 description', age_limited=False)
game2 = Game.objects.create(title='Game 2', cost=75.00, size=2.0, description='Game 2 description', age_limited=True)
game3 = Game.objects.create(title='Game 3', cost=100.00, size=3.0, description='Game 3 description', age_limited=False)

# Assign Buyer records to Game records
game1.buyer.set([buyer1, buyer2, buyer3])
game2.buyer.set([buyer1, buyer2])
game3.buyer.set([buyer1, buyer3])

# Ensure that only one Buyer has all Game.Buyer with age less than 18 and does not have games with age_limited=True
under_18_buyers = Buyer.objects.filter(age__lt=18)
if under_18_buyers.count() == 1:
    under_18_buyer = under_18_buyers.first()
    games_with_age_limit = Game.objects.filter(age_limited=True)
    if games_with_age_limit.count() > 0:
        games_with_age_limit.exclude(buyer=under_18_buyer).update(buyer=buyer1) 
"""    