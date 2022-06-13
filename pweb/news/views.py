from django.shortcuts import render, redirect

# Create your views here.
from .models import Game, App, SiteUser

def test(request):
    game = Game.objects.all()
    return render(request, 'home.html', {'games': game})


def home(request):
    if request.method == "POST" and request.POST['type'] == 'game':
        game = Game.objects.get(id=request.POST.get('id'))
        game.title = request.POST['edit_value']
        game.save()

    if request.method == "POST" and request.POST['type'] == 'app':
        app = App.objects.get(id=request.POST.get('id'))
        app.title = request.POST['edit_value']
        app.save()


    if request.user.is_authenticated:
        if request.user.is_publisher or request.user.is_user:
            user = SiteUser.objects.get(id=request.user.id)
            return render(request, 'home.html', {'games': Game.objects.all(), 'apps': App.objects.all()})

    return render(request, 'home.html', {'games': Game.objects.all(), 'apps': App.objects.all()})



def edit_game(request, post_id):
    if request.user.is_authenticated and request.user.is_publisher:
        game = Game.objects.get(id=post_id)
        return render(request, 'edit_game.html', {'game': game})
    
    return redirect('/')

def edit_app(request, post_id):
    if request.user.is_authenticated and request.user.is_publisher:
        app = App.objects.get(id=post_id)
        return render(request, 'edit_app.html', {'app': app})
    
    return redirect('/')
