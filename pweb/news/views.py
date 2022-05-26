from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, SiteUser

def test(request):
    post = Post.objects.all()

    return render(request, 'home.html', {'posts': post})


def home(request):
    #TODO check if authentificated and type of user
    if request.method == "POST":
        print(request.POST['edit_value'])
        print(request.POST.get('id'))

        post = Post.objects.get(id=request.POST.get('id'))
        post.title = request.POST['edit_value']
        post.save()


    if request.user.is_authenticated:
        if request.user.is_editor or request.user.is_subscriber:
            user = SiteUser.objects.get(id=request.user.id)
            post = Post.objects.all()

            print(user, '***')
            return render(request, 'home.html', {'posts': post})
    #

    post = Post.objects.filter(private=False)
    return render(request, 'home.html', {'posts': post})



def edit(request, post_id):
    if request.user.is_authenticated and request.user.is_editor:
        post = Post.objects.get(id=post_id)
        return render(request, 'edit.html', {'post': post})
    

    return redirect('/')

