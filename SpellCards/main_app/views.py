from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
# Create your views here.
from .models import Spell
from .forms import SpellForm, LoginForm


def index(request):
    spells = Spell.objects.all()
    form = SpellForm()
    return render(request, 'index.html', {'spells':spells, 'form':form})

def detail(request, spell_id):
    spell = Spell.objects.get(id=spell_id)
    return render(request, 'detail.html', {'spell':spell})

def post_spell(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SpellForm(data = request.POST, files = request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            spell = form.save(commit = False)
            spell.user = request.user
            spell.likes = 0
            spell.save()
        # redirect to a new URL:
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

def search(request):
    search_val = request.GET.get('search', None)

    if (search_val != None):
        results = []
        spells = Spell.objects.filter(name__icontains=search_val)
        for spell in spells:
            json = {}
            json['name'] = spell.name
            json['link'] = 'http://127.0.0.1:8000/index/' + str(spell.id) +'/'
            results.append(json)
        return JsonResponse({'results':results})
    else:
        return render(request, 'search.html')
