from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
from .models import Buyer, Game


def main(request):
    return render(request, 'second_task/main.html')

def games(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'second_task/store.html', context)

def cart(request):
    return render(request, 'second_task/cart.html')



def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        for user in users:
            if user.name != username and password == repeat_password:
                Buyer.objects.create(name=username, balance=0.0, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
            if user.name == username:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'second_task/registration_page.html', info)
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'second_task/registration_page.html', info)
    else:
        return render(request, 'second_task/registration_page.html')