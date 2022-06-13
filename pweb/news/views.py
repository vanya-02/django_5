from django.shortcuts import render, redirect

# Create your views here.
from .models import Game, App, SiteUser

def test(request):
    game = Game.objects.all()
    return render(request, 'home.html', {'games': game})


def home(request):
    if request.method == "POST" and request.POST['type'] == 'game':
        if request.POST['edit_title']:
            game = Game.objects.get(id=request.POST.get('id'))
            game.title = request.POST['edit_title']
            game.save()     
        if request.POST['edit_body']:
            game = Game.objects.get(id=request.POST.get('id'))
            game.body = request.POST['edit_body']
            game.save()  

    elif request.method == "POST" and request.POST['type'] == 'app':
        if request.POST['edit_title']:
            app = App.objects.get(id=request.POST.get('id'))
            app.title = request.POST['edit_title']
            app.save()     
        if request.POST['edit_body']:
            app = App.objects.get(id=request.POST.get('id'))
            app.body = request.POST['edit_body']
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

def add_app(request):
    if request.method == 'POST':
        title, body = request.POST['title'], request.POST['body']
        if title and body:
            new_entry = App(title=title, body=body)
            new_entry.save()

    return render(request, 'add_app.html')

def add_game(request):
    if request.method == 'POST':
        title, body = request.POST['title'], request.POST['body']
        if title and body:
            new_entry = Game(title=title, body=body)
            new_entry.save()

    return render(request, 'add_game.html')