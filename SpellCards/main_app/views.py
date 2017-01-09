from django.shortcuts import render
from .models import Spell
# Create your views here.


def testindex(request):

    return render(request, 'testindex.html', {'spells':spells})

def index(request):
    spells = Spell.objects.all()
    return render(request, 'index.html', {'spells':spells})

def detail(request, spell_id):
    spell = Spell.objects.get(id=spell_id)
    return render(request, 'detail.html', {'spell':spell})
