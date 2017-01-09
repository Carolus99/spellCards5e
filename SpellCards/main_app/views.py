from django.shortcuts import render
from django.http import HttpResponse
from .models import Spell
from .forms import SpellForm
# Create your views here.


def testindex(request):

    return render(request, 'testindex.html', {'spells':spells})

def index(request):
    spells = Spell.objects.all()
    form = SpellForm()
    return render(request, 'index.html', {'spells':spells, 'form':form})

def detail(request, spell_id):
    spell = Spell.objects.get(id=spell_id)
    return render(request, 'detail.html', {'spell':spell})

def post_spell(request):
    form = SpellForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit = True)
    return HttpResponseRedirect('/')
