from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Spell
from .forms import SpellForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from django.core.urlresolvers import reverse
# Create your views here.



def index(request):
    spells = Spell.objects.all()
    form = SpellForm()
    return render(request, 'index.html', {'spells':spells, 'form':form})

def detail(request, spell_id):
    spell = Spell.objects.get(id=spell_id)
    return render(request, 'detail.html', {'spell':spell})

def post_spell(request):
    form = SpellForm(request.POST)
    if form.is_valid():
        spell = form.save(commit=False)
        spell.user = request.user
        spell.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/index/')

def profile(request, username):
    user = User.objects.get(username=username)
    spells = Spell.objects.filter(user=user)
    return render(request, 'profile.html', {'username':username, 'spells':spells})

def login_view(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('http://127.0.0.1:8000/index/')
                else:
                    print("The account has been disabled!")
            else:
                print("The username and password were incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8000/index/')
